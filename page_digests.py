from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from datetime import date
from pathlib import Path, PurePosixPath
from urllib.parse import urljoin, urlsplit

import httpx

PAGE_DIGESTS_FILENAME = "page-digests.json"
PAGE_DIGESTS_VERSION = 1
_DIGEST_PATTERN = re.compile(r"[0-9a-f]{64}")
_DIGEST_FORMAT = b"sm-docs-page-markdown-v1\0"


def empty_page_digests() -> dict:
    return {"version": PAGE_DIGESTS_VERSION, "pages": {}}


def validate_page_digests(value: object, source: str = "page digests") -> dict:
    if not isinstance(value, dict):
        raise TypeError(f"Invalid {source}")
    if value.get("version") != PAGE_DIGESTS_VERSION:
        raise ValueError(f"Invalid {source} version")
    pages = value.get("pages")
    if not isinstance(pages, dict):
        raise TypeError(f"Invalid {source} pages")

    validated = empty_page_digests()
    for raw_path, raw_record in pages.items():
        if not isinstance(raw_path, str) or not raw_path:
            raise ValueError(f"Invalid page path in {source}")
        path = PurePosixPath(raw_path)
        if (
            path.is_absolute()
            or path.suffix != ".html"
            or any(part in {"", ".", ".."} for part in path.parts)
            or path.as_posix() != raw_path
        ):
            raise ValueError(f"Invalid page path in {source}: {raw_path!r}")
        if not isinstance(raw_record, dict):
            raise TypeError(f"Invalid record for {raw_path!r} in {source}")
        digest = raw_record.get("digest")
        lastmod = raw_record.get("lastmod")
        if not isinstance(digest, str) or _DIGEST_PATTERN.fullmatch(digest) is None:
            raise ValueError(f"Invalid digest for {raw_path!r} in {source}")
        if not isinstance(lastmod, str):
            raise TypeError(f"Invalid lastmod for {raw_path!r} in {source}")
        try:
            parsed_date = date.fromisoformat(lastmod)
        except ValueError as error:
            raise ValueError(f"Invalid lastmod for {raw_path!r} in {source}") from error
        if parsed_date.isoformat() != lastmod:
            raise ValueError(f"Invalid lastmod for {raw_path!r} in {source}")
        validated["pages"][raw_path] = {
            "digest": digest,
            "lastmod": lastmod,
        }
    return validated


def load_page_digests(
    path: Path | str,
    *,
    missing_ok: bool = False,
) -> dict:
    path = Path(path)
    if missing_ok and not path.exists():
        return empty_page_digests()
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"Invalid page digests file: {path}") from error
    return validate_page_digests(value, str(path))


def write_page_digests(path: Path | str, value: object) -> Path:
    path = Path(path)
    validated = validate_page_digests(value)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(validated, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def page_digest(path: Path | str) -> str:
    digest = hashlib.sha256()
    digest.update(_DIGEST_FORMAT)
    digest.update(Path(path).read_bytes())
    return digest.hexdigest()


def _manifest_url(site_url: str) -> str:
    parsed = urlsplit(site_url)
    if (
        parsed.scheme not in {"http", "https"}
        or not parsed.netloc
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("The deployed site URL must be an absolute HTTP(S) URL")
    return urljoin(f"{site_url.rstrip('/')}/", PAGE_DIGESTS_FILENAME)


def fetch_page_digests(
    site_url: str,
    *,
    transport: httpx.BaseTransport | None = None,
) -> dict:
    url = _manifest_url(site_url)
    with (
        httpx.Client(
            follow_redirects=True, timeout=30.0, transport=transport
        ) as client,
        client.stream(
            "GET",
            url,
            params={"check": str(time.time_ns())},
            headers={"Cache-Control": "no-cache"},
        ) as response,
    ):
        if response.status_code == 404:
            return empty_page_digests()
        response.raise_for_status()
        body = bytearray()
        for chunk in response.iter_bytes():
            body.extend(chunk)

    try:
        value = json.loads(body.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("Invalid deployed page digests") from error
    return validate_page_digests(value, "deployed page digests")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-url", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    try:
        page_digests = fetch_page_digests(args.site_url)
    except (TypeError, ValueError) as error:
        print(
            f"Warning: ignoring invalid deployed page digests: {error}",
            file=sys.stderr,
        )
        page_digests = empty_page_digests()

    output = write_page_digests(args.output, page_digests)
    print(f"Wrote previous page digests to {output}")


if __name__ == "__main__":
    main()
