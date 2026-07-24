from pathlib import Path

import httpx

MAX_DOWNLOAD_BYTES = 25 * 1024 * 1024


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
        with httpx.stream(
            "GET",
            url,
            follow_redirects=True,
            timeout=60.0,
        ) as response:
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
