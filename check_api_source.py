from __future__ import annotations

import argparse
import time
from pathlib import Path
from urllib.parse import urljoin, urlsplit

import httpx

from download_docs import SOURCE_HASH_FILENAME, load_downloaded, parse_source_digest

MAX_MARKER_BYTES = 256


def _marker_url(site_url: str) -> str:
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
    return urljoin(f"{site_url.rstrip('/')}/", SOURCE_HASH_FILENAME)


def fetch_deployed_digest(
    site_url: str,
    current_digest: str,
    *,
    transport: httpx.BaseTransport | None = None,
) -> str | None:
    current_digest = parse_source_digest(current_digest, "current API source")
    marker_url = _marker_url(site_url)
    with (
        httpx.Client(
            follow_redirects=True,
            timeout=30.0,
            transport=transport,
        ) as client,
        client.stream(
            "GET",
            marker_url,
            params={
                "source": current_digest,
                "check": str(time.time_ns()),
            },
            headers={"Cache-Control": "no-cache"},
        ) as response,
    ):
        if response.status_code == 404:
            return None
        response.raise_for_status()

        body = bytearray()
        for chunk in response.iter_bytes():
            body.extend(chunk)
            if len(body) > MAX_MARKER_BYTES:
                raise ValueError("The deployed API source marker is too large")

    try:
        marker = body.decode("ascii")
    except UnicodeDecodeError as error:
        raise ValueError("The deployed API source marker is not ASCII") from error

    return parse_source_digest(marker, f"deployed {SOURCE_HASH_FILENAME}")


def has_source_changed(
    site_url: str,
    current_digest: str,
    *,
    transport: httpx.BaseTransport | None = None,
) -> bool:
    deployed_digest = fetch_deployed_digest(
        site_url,
        current_digest,
        transport=transport,
    )
    return deployed_digest != current_digest


def _write_github_output(path: Path, digest: str, changed: bool) -> None:
    with path.open("a", encoding="utf-8") as output:
        output.write(f"digest={digest}\n")
        output.write(f"changed={str(changed).lower()}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--site-url", required=True)
    parser.add_argument("--github-output", type=Path, required=True)
    args = parser.parse_args()

    docs = load_downloaded(args.source_root)
    changed = has_source_changed(args.site_url, docs.source_digest)
    _write_github_output(args.github_output, docs.source_digest, changed)

    if changed:
        print("The deployed API source differs from the official source.")
    else:
        print("The deployed API source is current; deployment will be skipped.")


if __name__ == "__main__":
    main()
