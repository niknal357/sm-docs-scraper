from __future__ import annotations

import asyncio
from html import unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
from urllib.parse import unquote

from pagefind.index import IndexConfig, PagefindIndex

from symbol_catalog import Symbol, SymbolCatalog


SYMBOL_INDEX_NAME = "search-symbols.json"
PAGEFIND_DIRECTORY = "pagefind"


class _ElementIds(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        element_id = dict(attrs).get("id")
        if element_id is not None:
            self.ids.add(element_id)


def _plain_text(value: str) -> str:
    value = re.sub(r"<[^>]*>", "", value)
    return " ".join(unescape(value).split())


def _record(symbol: Symbol) -> dict[str, str]:
    page_name = "Global" if symbol.page_name == "GLOBAL" else symbol.page_name
    return {
        "id": symbol.id,
        "qualifiedName": symbol.qualified_name,
        "name": symbol.name,
        "aliases": "\n".join(symbol.aliases),
        "parentPage": page_name,
        "signature": "\n".join(symbol.signatures),
        "summary": _plain_text(symbol.summary),
        "types": " ".join((*symbol.parameter_types, *symbol.return_types)),
        "parameterTypes": ", ".join(symbol.parameter_types),
        "returnTypes": ", ".join(symbol.return_types),
        "environment": symbol.environment,
        "kind": symbol.kind,
        "pageKind": symbol.page_kind,
        "availability": ", ".join(symbol.availability),
        "url": symbol.url,
    }


def write_symbol_index(catalog: SymbolCatalog, html_root: Path) -> Path:
    output_path = html_root / "assets" / SYMBOL_INDEX_NAME
    records = [_record(symbol) for symbol in catalog.symbols]
    payload = {"version": 1, "records": records}
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    return output_path


def validate_symbol_urls(catalog: SymbolCatalog, html_root: Path) -> None:
    ids_by_path: dict[Path, set[str]] = {}
    record_ids: set[str] = set()
    errors: list[str] = []

    for symbol in catalog.symbols:
        if symbol.id in record_ids:
            errors.append(f"duplicate symbol ID: {symbol.id}")
        record_ids.add(symbol.id)

        url_path, _, fragment = symbol.url.partition("#")
        target = html_root / unquote(url_path)
        if not target.is_file():
            errors.append(f"{symbol.id}: missing search target: {symbol.url}")
            continue
        if not fragment:
            continue

        element_ids = ids_by_path.get(target)
        if element_ids is None:
            parser = _ElementIds()
            parser.feed(target.read_text(encoding="utf-8"))
            element_ids = parser.ids
            ids_by_path[target] = element_ids
        if unquote(fragment) not in element_ids:
            errors.append(f"{symbol.id}: missing search fragment: {symbol.url}")

    if errors:
        displayed = errors[:50]
        if len(errors) > len(displayed):
            displayed.append(f"... and {len(errors) - len(displayed)} more")
        raise ValueError("Symbol index validation failed:\n- " + "\n- ".join(displayed))


async def _write_pagefind_index(html_root: Path) -> Path:
    output_path = html_root / "assets" / PAGEFIND_DIRECTORY
    shutil.rmtree(output_path, ignore_errors=True)
    config = IndexConfig(
        output_path=str(output_path),
        include_characters=".:",
        force_language="en",
        keep_index_url=True,
    )
    async with PagefindIndex(config=config) as index:
        result = await index.add_directory(str(html_root))
        if result["page_count"] == 0:
            raise ValueError("Pagefind did not find any searchable pages")
    return output_path


def build_search_indexes(
    catalog: SymbolCatalog, html_root: Path | str
) -> tuple[Path, Path]:
    html_root = Path(html_root)
    symbol_path = write_symbol_index(catalog, html_root)
    validate_symbol_urls(catalog, html_root)
    pagefind_path = asyncio.run(_write_pagefind_index(html_root))
    return symbol_path, pagefind_path
