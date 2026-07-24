import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

import httpx

from check_api_source import fetch_deployed_digest, has_source_changed
from download_docs import (
    JSON_DOCS_URL,
    LUA_DOCS_URL,
    SOURCE_HASH_FILENAME,
    download,
    hash_json_docs,
    load_downloaded,
    write_source_digest,
)


class SourceDigestTests(unittest.TestCase):
    def test_hash_is_deterministic_for_paths_and_contents(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = root / "first"
            second = root / "second"
            first.mkdir()
            second.mkdir()

            (first / "index.json").write_text('{"Game": {}}', encoding="utf-8")
            (first / "page.json").write_text('{"name": "test"}', encoding="utf-8")
            (second / "page.json").write_text('{"name": "test"}', encoding="utf-8")
            (second / "index.json").write_text('{"Game": {}}', encoding="utf-8")
            os.utime(first / "index.json", (1, 1))
            os.utime(second / "index.json", (2, 2))

            self.assertEqual(hash_json_docs(first), hash_json_docs(second))

            (second / "page.json").write_text('{"name": "changed"}', encoding="utf-8")
            self.assertNotEqual(hash_json_docs(first), hash_json_docs(second))

    def test_load_rejects_source_changed_after_digest_was_written(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            json_docs = root / "json"
            json_docs.mkdir()
            index = json_docs / "index.json"
            index.write_text("{}", encoding="utf-8")
            (root / "sm.lua").write_text("return {}\n", encoding="utf-8")
            write_source_digest(root, hash_json_docs(json_docs))

            load_downloaded(root)
            index.write_text('{"Game": {}}', encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "does not match"):
                load_downloaded(root)


class ArchiveValidationTests(unittest.TestCase):
    def _copy_archives(self, json_zip: Path, lua_zip: Path):
        def copy(url: str, destination: Path) -> None:
            source = json_zip if url == JSON_DOCS_URL else lua_zip
            self.assertIn(url, {JSON_DOCS_URL, LUA_DOCS_URL})
            shutil.copyfile(source, destination)

        return copy

    def test_download_validates_and_records_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            json_zip = root / "source-json.zip"
            lua_zip = root / "source-lua.zip"
            with ZipFile(json_zip, "w") as archive:
                archive.writestr("json/index.json", "{}")
            with ZipFile(lua_zip, "w") as archive:
                archive.writestr("sm.lua", "return {}\n")

            destination = root / "downloaded"
            with patch(
                "download_docs.download_file",
                side_effect=self._copy_archives(json_zip, lua_zip),
            ):
                docs = download(destination)

            self.assertEqual(docs, load_downloaded(destination))
            self.assertTrue((destination / SOURCE_HASH_FILENAME).is_file())

    def test_download_rejects_parent_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            json_zip = root / "source-json.zip"
            lua_zip = root / "source-lua.zip"
            with ZipFile(json_zip, "w") as archive:
                archive.writestr("json/../../escaped.json", "{}")
            with ZipFile(lua_zip, "w") as archive:
                archive.writestr("sm.lua", "return {}\n")

            with (
                patch(
                    "download_docs.download_file",
                    side_effect=self._copy_archives(json_zip, lua_zip),
                ),
                self.assertRaisesRegex(ValueError, "Unsafe archive path"),
            ):
                download(root / "downloaded")

            self.assertFalse((root / "escaped.json").exists())


class DeployedSourceTests(unittest.TestCase):
    digest = "a" * 64

    def test_matching_deployed_digest_skips_update(self) -> None:
        requests = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, text=f"{self.digest}\n")

        transport = httpx.MockTransport(handler)
        changed = has_source_changed(
            "https://example.test/docs",
            self.digest,
            transport=transport,
        )

        self.assertFalse(changed)
        self.assertEqual(requests[0].url.path, "/docs/api-source.sha256")
        self.assertEqual(requests[0].url.params["source"], self.digest)
        self.assertEqual(requests[0].headers["cache-control"], "no-cache")

    def test_missing_deployed_digest_triggers_update(self) -> None:
        transport = httpx.MockTransport(
            lambda request: httpx.Response(404, request=request)
        )

        self.assertTrue(
            has_source_changed(
                "https://example.test/",
                self.digest,
                transport=transport,
            )
        )

    def test_invalid_deployed_digest_fails_check(self) -> None:
        transport = httpx.MockTransport(
            lambda request: httpx.Response(200, text="not-a-digest", request=request)
        )

        with self.assertRaisesRegex(ValueError, "Invalid source digest"):
            fetch_deployed_digest(
                "https://example.test/",
                self.digest,
                transport=transport,
            )

    def test_deployed_site_error_fails_check(self) -> None:
        transport = httpx.MockTransport(
            lambda request: httpx.Response(503, request=request)
        )

        with self.assertRaises(httpx.HTTPStatusError):
            fetch_deployed_digest(
                "https://example.test/",
                self.digest,
                transport=transport,
            )


if __name__ == "__main__":
    unittest.main()
