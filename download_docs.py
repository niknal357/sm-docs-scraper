from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile, ZipInfo

from download_file import download_file

JSON_DOCS_URL = "https://scrapmechanic.com/api/json.zip"
LUA_DOCS_URL = "https://scrapmechanic.com/api/lua.zip"
SOURCE_HASH_FILENAME = "api-source.sha256"
MAX_ARCHIVE_MEMBERS = 5_000
MAX_ARCHIVE_MEMBER_BYTES = 25 * 1024 * 1024
MAX_ARCHIVE_UNCOMPRESSED_BYTES = 100 * 1024 * 1024
_HASH_PATTERN = re.compile(r"[0-9a-f]{64}")
_HASH_FORMAT = b"sm-docs-json-source-v1\0"


@dataclass(frozen=True)
class DownloadedDocs:
    root: Path
    json_docs: Path
    lua_docs: Path
    source_digest: str


def _member_parts(info: ZipInfo) -> tuple[str, ...]:
    name = info.filename
    if not name or "\\" in name or name.startswith("/"):
        raise ValueError(f"Unsafe archive path: {name!r}")

    trimmed_name = name[:-1] if info.is_dir() else name
    parts = tuple(trimmed_name.split("/"))
    if not trimmed_name or any(part in {"", ".", ".."} for part in parts):
        raise ValueError(f"Unsafe archive path: {name!r}")

    path = PurePosixPath(*parts)
    if path.is_absolute():
        raise ValueError(f"Unsafe archive path: {name!r}")
    return parts


def _validate_member_type(info: ZipInfo) -> None:
    mode = info.external_attr >> 16
    file_type = stat.S_IFMT(mode)
    if file_type not in {0, stat.S_IFREG, stat.S_IFDIR}:
        raise ValueError(f"Unsupported archive member type: {info.filename!r}")
    if file_type == stat.S_IFDIR and not info.is_dir():
        raise ValueError(f"Invalid directory entry: {info.filename!r}")
    if file_type == stat.S_IFREG and info.is_dir():
        raise ValueError(f"Invalid file entry: {info.filename!r}")


def _validate_archive_members(
    archive: ZipFile,
    archive_kind: str,
) -> list[tuple[ZipInfo, tuple[str, ...]]]:
    infos = archive.infolist()
    if not infos:
        raise ValueError(f"The {archive_kind} archive is empty")
    if len(infos) > MAX_ARCHIVE_MEMBERS:
        raise ValueError(f"The {archive_kind} archive contains too many files")

    members: list[tuple[ZipInfo, tuple[str, ...]]] = []
    names: set[str] = set()
    total_size = 0
    regular_files = 0

    for info in infos:
        if info.flag_bits & 0x1:
            raise ValueError(
                f"Encrypted archive member is not supported: {info.filename!r}"
            )
        _validate_member_type(info)
        parts = _member_parts(info)
        normalized_name = "/".join(parts)
        if normalized_name in names:
            raise ValueError(f"Duplicate archive path: {info.filename!r}")
        names.add(normalized_name)

        if info.file_size > MAX_ARCHIVE_MEMBER_BYTES:
            raise ValueError(f"Archive member is too large: {info.filename!r}")
        total_size += info.file_size
        if total_size > MAX_ARCHIVE_UNCOMPRESSED_BYTES:
            raise ValueError(f"The {archive_kind} archive is too large")

        if archive_kind == "JSON":
            if parts[0] != "json":
                raise ValueError(f"Unexpected path in JSON archive: {info.filename!r}")
            if not info.is_dir():
                if len(parts) < 2 or not parts[-1].endswith(".json"):
                    raise ValueError(
                        f"Unexpected file in JSON archive: {info.filename!r}"
                    )
                regular_files += 1
        elif archive_kind == "Lua":
            if info.is_dir() or parts != ("sm.lua",):
                raise ValueError(f"Unexpected path in Lua archive: {info.filename!r}")
            regular_files += 1
        else:
            raise ValueError(f"Unknown archive kind: {archive_kind}")

        members.append((info, parts))

    if regular_files == 0:
        raise ValueError(f"The {archive_kind} archive contains no files")
    return members


def _extract_archive(
    archive_path: Path,
    destination: Path,
    archive_kind: str,
) -> None:
    try:
        with ZipFile(archive_path) as archive:
            members = _validate_archive_members(archive, archive_kind)
            destination_root = destination.resolve()
            for info, parts in members:
                output_path = destination.joinpath(*parts)
                try:
                    output_path.resolve().relative_to(destination_root)
                except ValueError as error:
                    raise ValueError(
                        f"Unsafe archive path: {info.filename!r}"
                    ) from error
                if info.is_dir():
                    output_path.mkdir(parents=True, exist_ok=True)
                    continue

                output_path.parent.mkdir(parents=True, exist_ok=True)
                if output_path.exists():
                    raise ValueError(f"Archive path already exists: {info.filename!r}")

                written = 0
                with archive.open(info) as source, output_path.open("xb") as output:
                    while chunk := source.read(64 * 1024):
                        written += len(chunk)
                        if written > info.file_size:
                            raise ValueError(
                                f"Archive member exceeded its declared size: "
                                f"{info.filename!r}"
                            )
                        output.write(chunk)
                if written != info.file_size:
                    raise ValueError(f"Archive member size mismatch: {info.filename!r}")
    except BadZipFile as error:
        raise ValueError(f"Invalid {archive_kind} ZIP archive") from error


def _validate_downloaded_docs(root: Path) -> tuple[Path, Path]:
    json_docs = root / "json"
    lua_docs = root / "sm.lua"
    if json_docs.is_symlink() or not json_docs.is_dir():
        raise ValueError("Downloaded documentation has no json directory")
    if lua_docs.is_symlink() or not lua_docs.is_file() or lua_docs.stat().st_size == 0:
        raise ValueError("Downloaded documentation has no sm.lua file")

    json_entries = list(json_docs.rglob("*"))
    if any(path.is_symlink() for path in json_entries):
        raise ValueError("Downloaded documentation contains a symbolic link")
    json_files = sorted(path for path in json_entries if path.is_file())
    if not json_files or json_docs / "index.json" not in json_files:
        raise ValueError("Downloaded documentation has no JSON index")

    for path in json_files:
        if path.is_symlink() or path.suffix != ".json":
            raise ValueError(f"Unexpected documentation file: {path}")
        try:
            with path.open(encoding="utf-8") as file:
                value = json.load(file)
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError(f"Invalid JSON documentation file: {path}") from error
        if not isinstance(value, dict):
            raise TypeError(f"JSON documentation file is not an object: {path}")

    return json_docs, lua_docs


def hash_json_docs(json_docs: Path | str) -> str:
    json_docs = Path(json_docs)
    files = sorted(
        (path for path in json_docs.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(json_docs).as_posix(),
    )
    if not files:
        raise ValueError(f"No documentation files found in {json_docs}")

    digest = hashlib.sha256()
    digest.update(_HASH_FORMAT)
    for path in files:
        relative_path = path.relative_to(json_docs).as_posix().encode("utf-8")
        digest.update(len(relative_path).to_bytes(4, "big"))
        digest.update(relative_path)
        size = path.stat().st_size
        digest.update(size.to_bytes(8, "big"))
        with path.open("rb") as file:
            while chunk := file.read(64 * 1024):
                digest.update(chunk)
    return digest.hexdigest()


def parse_source_digest(value: str, source: str = "source digest") -> str:
    digest = value.strip()
    if _HASH_PATTERN.fullmatch(digest) is None:
        raise ValueError(f"Invalid source digest in {source}")
    return digest


def read_source_digest(path: Path | str) -> str:
    path = Path(path)
    return parse_source_digest(path.read_text(encoding="ascii"), str(path))


def write_source_digest(directory: Path | str, digest: str) -> Path:
    digest = parse_source_digest(digest)
    path = Path(directory) / SOURCE_HASH_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"{digest}\n", encoding="ascii")
    return path


def load_downloaded(root: Path | str) -> DownloadedDocs:
    root = Path(root)
    json_docs, lua_docs = _validate_downloaded_docs(root)
    source_digest = hash_json_docs(json_docs)
    recorded_digest = read_source_digest(root / SOURCE_HASH_FILENAME)
    if source_digest != recorded_digest:
        raise ValueError("Downloaded documentation does not match its source digest")
    return DownloadedDocs(root, json_docs, lua_docs, source_digest)


def _safe_destination(destination: Path | str) -> Path:
    requested_destination = Path(destination)
    if requested_destination.is_symlink():
        raise ValueError(
            f"Documentation destination is a symbolic link: {requested_destination}"
        )
    destination = requested_destination.resolve()
    protected_paths = {
        Path(destination.anchor),
        Path.cwd().resolve(),
        Path.home().resolve(),
    }
    if destination in protected_paths:
        raise ValueError(f"Refusing to replace protected directory: {destination}")
    if destination.exists() and (destination.is_symlink() or not destination.is_dir()):
        raise ValueError(f"Documentation destination is not a directory: {destination}")
    return destination


def download(destination: Path | str = "temp") -> DownloadedDocs:
    destination = _safe_destination(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(
        tempfile.mkdtemp(
            prefix=f".{destination.name}-download-",
            dir=destination.parent,
        )
    )

    try:
        json_zip = staging / "json.zip"
        lua_zip = staging / "lua.zip"
        download_file(JSON_DOCS_URL, json_zip)
        download_file(LUA_DOCS_URL, lua_zip)
        _extract_archive(json_zip, staging, "JSON")
        _extract_archive(lua_zip, staging, "Lua")

        json_docs, _ = _validate_downloaded_docs(staging)
        source_digest = hash_json_docs(json_docs)
        write_source_digest(staging, source_digest)

        if destination.exists():
            shutil.rmtree(destination)
        staging.replace(destination)
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise

    return load_downloaded(destination)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", type=Path, default=Path("temp"))
    args = parser.parse_args()

    docs = download(args.destination)
    print(f"Downloaded JSON docs to {docs.json_docs}")
    print(f"Downloaded Lua docs to {docs.lua_docs}")
    print(f"API source digest: {docs.source_digest}")


if __name__ == "__main__":
    main()
