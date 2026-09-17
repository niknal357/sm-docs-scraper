import ssl
from datetime import UTC, datetime
from pathlib import Path

import httpx

MAX_DOWNLOAD_BYTES = 25 * 1024 * 1024
CERTIFICATE_GRACE_DEADLINE = datetime(2026, 12, 8, 5, 1, 1, tzinfo=UTC)
# OpenSSL X509_V_FLAG_NO_CHECK_TIME is not named in Python's ssl module.
_X509_V_FLAG_NO_CHECK_TIME = 0x200000
_X509_V_ERR_CERT_HAS_EXPIRED = 10


def _is_expired_certificate(error: BaseException) -> bool:
    seen: set[int] = set()
    while id(error) not in seen:
        seen.add(id(error))
        if isinstance(error, ssl.SSLCertVerificationError):
            return error.verify_code == _X509_V_ERR_CERT_HAS_EXPIRED
        cause = error.__cause__ or error.__context__
        if cause is None:
            break
        error = cause
    return False


class _ExpiryGraceTransport(httpx.BaseTransport):
    def __init__(self) -> None:
        self._normal = httpx.HTTPTransport()
        self._grace: httpx.HTTPTransport | None = None

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        try:
            return self._normal.handle_request(request)
        except httpx.ConnectError as error:
            if not (
                request.url.scheme == "https"
                and request.url.host == "scrapmechanic.com"
                and request.url.port in {None, 443}
                and datetime.now(UTC) < CERTIFICATE_GRACE_DEADLINE
                and _is_expired_certificate(error)
            ):
                raise

        if self._grace is None:
            context = httpx.create_ssl_context()
            # Keep CA, signature and hostname checks; relax dates only after expiry.
            context.verify_flags |= _X509_V_FLAG_NO_CHECK_TIME
            self._grace = httpx.HTTPTransport(verify=context)
        return self._grace.handle_request(request)

    def close(self) -> None:
        try:
            self._normal.close()
        finally:
            if self._grace is not None:
                self._grace.close()


def download_file(
    url: str,
    destination: Path,
    *,
    max_bytes: int = MAX_DOWNLOAD_BYTES,
) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    partial = destination.with_name(f"{destination.name}.part")
    partial.unlink(missing_ok=True)
    downloaded = 0

    try:
        with (
            httpx.Client(
                transport=_ExpiryGraceTransport(),
                follow_redirects=True,
                timeout=60.0,
            ) as client,
            client.stream("GET", url) as response,
        ):
            response.raise_for_status()
            if url.startswith("https://") and response.url.scheme != "https":
                raise ValueError(f"Download from {url} redirected to an insecure URL")
            content_length = response.headers.get("content-length")
            if content_length is not None:
                try:
                    expected_size = int(content_length)
                except ValueError as error:
                    raise ValueError(f"Invalid Content-Length for {url}") from error
                if expected_size < 0:
                    raise ValueError(f"Invalid Content-Length for {url}")
                if expected_size > max_bytes:
                    raise ValueError(f"Download from {url} exceeds {max_bytes} bytes")

            with partial.open("wb") as file:
                for chunk in response.iter_bytes():
                    downloaded += len(chunk)
                    if downloaded > max_bytes:
                        raise ValueError(
                            f"Download from {url} exceeds {max_bytes} bytes"
                        )
                    file.write(chunk)

        if downloaded == 0:
            raise ValueError(f"Download from {url} was empty")
        partial.replace(destination)
    finally:
        partial.unlink(missing_ok=True)
