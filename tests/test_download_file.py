import ssl
import tempfile
import unittest
from datetime import UTC, datetime, timedelta
from pathlib import Path
from unittest.mock import Mock, patch

import httpx

from download_file import (
    CERTIFICATE_GRACE_DEADLINE,
    _ExpiryGraceTransport,
    _is_expired_certificate,
    download_file,
)

URL = "https://scrapmechanic.com/api/json.zip"


def certificate_error(code: int = 10) -> httpx.ConnectError:
    certificate = ssl.SSLCertVerificationError(1, "certificate verification failed")
    certificate.verify_code = code
    wrapped = RuntimeError("TLS handshake failed")
    wrapped.__cause__ = certificate
    error = httpx.ConnectError("connection failed")
    error.__cause__ = wrapped
    return error


class ExpiryGraceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.normal = Mock(spec=httpx.HTTPTransport)
        self.grace = Mock(spec=httpx.HTTPTransport)
        self.factory = self.enterContext(
            patch(
                "download_file.httpx.HTTPTransport",
                side_effect=[self.normal, self.grace],
            )
        )
        self.clock = self.enterContext(patch("download_file.datetime"))
        self.clock.now.return_value = datetime(2026, 9, 16, tzinfo=UTC)
        self.transport = _ExpiryGraceTransport()
        self.addCleanup(self.transport.close)
        self.request = httpx.Request("GET", URL)

    def test_valid_certificate_uses_normal_verification_only(self) -> None:
        self.assertIs(
            self.transport.handle_request(self.request),
            self.normal.handle_request.return_value,
        )
        self.assertEqual(self.factory.call_count, 1)
        self.grace.handle_request.assert_not_called()

    def test_expiry_retries_with_chain_and_hostname_checks_enabled(self) -> None:
        self.normal.handle_request.side_effect = certificate_error()
        self.assertIs(
            self.transport.handle_request(self.request),
            self.grace.handle_request.return_value,
        )
        context = self.factory.call_args.kwargs["verify"]
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
        self.assertTrue(context.check_hostname)
        self.assertTrue(context.verify_flags & 0x200000)
        self.normal.handle_request.assert_called_once_with(self.request)
        self.grace.handle_request.assert_called_once_with(self.request)

    def test_other_errors_never_retry(self) -> None:
        errors = [
            certificate_error(9),  # Not yet valid.
            certificate_error(18),  # Self-signed.
            certificate_error(20),  # Unknown issuer.
            certificate_error(62),  # Hostname mismatch.
            httpx.ConnectError("certificate has expired"),
            httpx.ConnectTimeout("timed out"),
        ]
        for error in errors:
            with self.subTest(error=error):
                self.normal.handle_request.side_effect = error
                with self.assertRaises(type(error)) as raised:
                    self.transport.handle_request(self.request)
                self.assertIs(raised.exception, error)
        self.assertEqual(self.factory.call_count, 1)

    def test_exception_is_limited_to_exact_https_origin(self) -> None:
        self.normal.handle_request.side_effect = certificate_error()
        for url in (
            "http://scrapmechanic.com/api/json.zip",
            "https://www.scrapmechanic.com/api/json.zip",
            "https://scrapmechanic.com.example.org/api/json.zip",
            "https://example.org/api/json.zip",
            "https://scrapmechanic.com:8443/api/json.zip",
        ):
            with self.subTest(url=url), self.assertRaises(httpx.ConnectError):
                self.transport.handle_request(httpx.Request("GET", url))
        self.assertEqual(self.factory.call_count, 1)

    def test_deadline_applies_even_after_fallback_connection_was_created(self) -> None:
        self.normal.handle_request.side_effect = certificate_error()
        self.clock.now.return_value = CERTIFICATE_GRACE_DEADLINE - timedelta(seconds=1)
        self.transport.handle_request(self.request)
        for when in (
            CERTIFICATE_GRACE_DEADLINE,
            CERTIFICATE_GRACE_DEADLINE + timedelta(days=1),
        ):
            with self.subTest(when=when):
                self.clock.now.return_value = when
                with self.assertRaises(httpx.ConnectError):
                    self.transport.handle_request(self.request)
        self.grace.handle_request.assert_called_once()

    def test_fallback_failure_is_not_retried(self) -> None:
        self.normal.handle_request.side_effect = certificate_error()
        self.grace.handle_request.side_effect = certificate_error(62)
        with self.assertRaises(httpx.ConnectError):
            self.transport.handle_request(self.request)
        self.grace.handle_request.assert_called_once()

    def test_every_request_tries_normal_verification_first(self) -> None:
        self.normal.handle_request.side_effect = [
            certificate_error(),
            httpx.Response(200),
        ]
        self.transport.handle_request(self.request)
        self.transport.handle_request(self.request)
        self.assertEqual(self.normal.handle_request.call_count, 2)
        self.grace.handle_request.assert_called_once()

    def test_redirect_to_another_host_does_not_get_exception(self) -> None:
        self.normal.handle_request.side_effect = certificate_error()
        self.grace.handle_request.return_value = httpx.Response(
            302, headers={"Location": "https://example.org/json.zip"}
        )
        with (
            httpx.Client(
                transport=self.transport, follow_redirects=True, trust_env=False
            ) as client,
            self.assertRaises(httpx.ConnectError),
        ):
            client.get(URL)
        self.assertEqual(self.normal.handle_request.call_count, 2)
        self.grace.handle_request.assert_called_once()

    def test_close_releases_both_connection_pools(self) -> None:
        self.normal.handle_request.side_effect = certificate_error()
        self.transport.handle_request(self.request)
        self.transport.close()
        self.normal.close.assert_called_once()
        self.grace.close.assert_called_once()

    def test_exception_context_and_cycles(self) -> None:
        error = certificate_error()
        error.__context__ = error.__cause__
        error.__cause__ = None
        self.assertTrue(_is_expired_certificate(error))
        error.__context__ = error
        self.assertFalse(_is_expired_certificate(error))


class DownloadTests(unittest.TestCase):
    def test_download_still_accepts_changing_content(self) -> None:
        contents = iter([b"first archive", b"updated archive"])
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "json.zip"
            for expected in (b"first archive", b"updated archive"):
                with patch(
                    "download_file._ExpiryGraceTransport",
                    return_value=httpx.MockTransport(
                        lambda request: httpx.Response(200, content=next(contents))
                    ),
                ):
                    download_file(URL, destination)
                self.assertEqual(destination.read_bytes(), expected)
                self.assertFalse(destination.with_name("json.zip.part").exists())

    def test_failed_download_keeps_previous_file_and_cleans_partial(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "json.zip"
            destination.write_bytes(b"previous archive")
            with (
                patch(
                    "download_file._ExpiryGraceTransport",
                    return_value=httpx.MockTransport(
                        lambda request: httpx.Response(200, content=b"too large")
                    ),
                ),
                self.assertRaisesRegex(ValueError, "exceeds"),
            ):
                download_file(URL, destination, max_bytes=1)
            self.assertEqual(destination.read_bytes(), b"previous archive")
            self.assertFalse(destination.with_name("json.zip.part").exists())


if __name__ == "__main__":
    unittest.main()
