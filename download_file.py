from pathlib import Path
import httpx

def download_file(url: str, destination: Path):
    with httpx.stream(
        "GET",
        url,
        follow_redirects = True,
        timeout = 60.0,
    ) as response:
        response.raise_for_status()
        with destination.open("wb") as file:
            for chunk in response.iter_bytes():
                file.write(chunk)
