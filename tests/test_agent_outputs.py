import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

import httpx

from make_ir import (
    Doc,
    Documentation,
    Entry,
    Environment,
    MetaOperation,
    Page,
    Parameter,
    parse_inline,
)
from page_digests import (
    fetch_page_digests,
    load_page_digests,
    main as page_digests_main,
)
from render_html import HtmlRenderer
from render_markdown import MarkdownRenderer


class SymbolPageTests(unittest.TestCase):
    def test_writes_aggregated_symbols_and_exact_callback_pages(self) -> None:
        game_new = Entry(
            name="new",
            doc=Doc(
                content=[
                    {
                        "type": "paragraph",
                        "content": parse_inline("Creates a [sm.color] value."),
                    }
                ],
                parameters=[Parameter("value", ["number"], [])],
            ),
        )
        game_new_from_string = Entry(
            name="new",
            doc=Doc(
                content=[{"type": "paragraph", "content": ["String overload."]}],
                parameters=[Parameter("value", ["string"], [])],
            ),
        )
        terrain_new = Entry(
            name="new",
            doc=Doc(
                content=[{"type": "paragraph", "content": ["Terrain overload."]}],
                parameters=[Parameter("value", ["string"], [])],
            ),
        )
        callback = Entry(
            name="client_onUpdate",
            callback_type="event",
            doc=Doc(
                content=[{"type": "paragraph", "content": ["Called every frame."]}]
            ),
        )
        server_callback = Entry(
            name="server_onUpdate",
            callback_type="event",
            doc=Doc(content=[{"type": "paragraph", "content": ["Called every tick."]}]),
        )
        game_namespace = Page(
            name="sm.color",
            source="game.json",
            functions=[game_new, game_new_from_string],
        )
        terrain_namespace = Page(
            name="sm.color", source="terrain.json", functions=[terrain_new]
        )
        character_class = Page(
            name="CharacterClass",
            source="character.json",
            callbacks=[callback, server_callback],
        )
        game = Environment(
            name="Game",
            namespaces=[game_namespace],
            classes=[character_class],
        )
        terrain = Environment(name="Terrain", namespaces=[terrain_namespace])
        docs = Documentation(version=1, environments=[game, terrain])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            markdown_root = root / "markdown"
            html_root = root / "html"
            renderer = MarkdownRenderer(docs, markdown_root, html_root)
            renderer._write_page(game, "namespace", game_namespace)
            renderer._write_page(terrain, "namespace", terrain_namespace)
            renderer._write_page(game, "class", character_class)
            renderer._write_symbol_pages()
            HtmlRenderer(docs, markdown_root, html_root)._write_html_tree()

            color_markdown = (markdown_root / "symbols" / "sm.color.new.md").read_text()
            callback_markdown = (
                markdown_root / "symbols" / "CharacterClass.client_onUpdate.md"
            ).read_text()
            color_html = (html_root / "symbols" / "sm.color.new.html").read_text()

            self.assertTrue((html_root / "symbols" / "sm.color.new.md").is_file())
            self.assertTrue(
                (
                    html_root / "symbols" / "CharacterClass.server_onUpdate.html"
                ).is_file()
            )
            self.assertFalse(
                (html_root / "symbols" / "CharacterClass.onUpdate.html").exists()
            )

        self.assertIn("**Environments:** Game, Terrain", color_markdown)
        self.assertIn("## Game", color_markdown)
        self.assertIn("## Terrain", color_markdown)
        self.assertIn(
            "Creates a [sm.color](../Game-Script-Environment/Static-Functions/"
            "sm.color.md) value.",
            color_markdown,
        )
        self.assertIn("### Game overload 1", color_markdown)
        self.assertIn("### Game overload 2", color_markdown)
        self.assertEqual(color_markdown.count("sm.color.new( value )"), 3)
        self.assertIn("**Callback side:** Client", callback_markdown)
        self.assertIn("CharacterClass:client_onUpdate", callback_markdown)
        self.assertIn(
            '<link rel="alternate" type="text/markdown" href="sm.color.new.md">',
            color_html,
        )

    def test_writes_operation_expressions_and_return_types(self) -> None:
        operation = Entry(
            name="__div",
            doc=Doc(
                operations=[
                    MetaOperation(
                        signature=parse_inline("[Color],number,[Color]"),
                        description=["Divides a color by a scalar."],
                    )
                ]
            ),
        )
        color = Page(name="Color", source="color.json", metamethods=[operation])
        game = Environment(name="Game", userdata=[color])
        docs = Documentation(version=1, environments=[game])

        with tempfile.TemporaryDirectory() as directory:
            markdown_root = Path(directory) / "markdown"
            markdown_root.mkdir()
            renderer = MarkdownRenderer(docs, markdown_root, Path(directory) / "html")
            renderer._write_symbol_pages()
            operation_markdown = (
                markdown_root / "symbols" / "Color.__div.md"
            ).read_text()

        self.assertIn("| Operation | Returns | Description |", operation_markdown)
        self.assertIn(
            "| `Color / number` | "
            "[Color](../Game-Script-Environment/Userdata/Color.md) | "
            "Divides a color by a scalar. |",
            operation_markdown,
        )
        self.assertNotIn("Color],number", operation_markdown)


class PageDigestFetchTests(unittest.TestCase):
    def test_missing_deployed_digests_returns_an_empty_manifest(self) -> None:
        transport = httpx.MockTransport(
            lambda request: httpx.Response(404, request=request)
        )

        manifest = fetch_page_digests(
            "https://example.test/docs",
            transport=transport,
        )

        self.assertEqual(manifest, {"version": 1, "pages": {}})

    def test_fetches_and_validates_deployed_digests(self) -> None:
        requests = []
        payload = {
            "version": 1,
            "pages": {
                "index.html": {
                    "digest": "a" * 64,
                    "lastmod": "2026-01-02",
                }
            },
        }

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json=payload, request=request)

        manifest = fetch_page_digests(
            "https://example.test/docs",
            transport=httpx.MockTransport(handler),
        )

        self.assertEqual(manifest, payload)
        self.assertEqual(requests[0].url.path, "/docs/page-digests.json")
        self.assertEqual(requests[0].headers["cache-control"], "no-cache")

    def test_command_ignores_invalid_deployed_digests(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "previous-page-digests.json"
            arguments = [
                "page_digests.py",
                "--site-url",
                "https://example.test/docs",
                "--output",
                str(output_path),
            ]
            with (
                patch("sys.argv", arguments),
                patch(
                    "page_digests.fetch_page_digests",
                    side_effect=ValueError("Invalid deployed page digests version"),
                ),
                patch("builtins.print") as output,
            ):
                page_digests_main()

            manifest = load_page_digests(output_path)

        self.assertEqual(manifest, {"version": 1, "pages": {}})
        output.assert_any_call(
            "Warning: ignoring invalid deployed page digests: "
            "Invalid deployed page digests version",
            file=sys.stderr,
        )


class PageLastmodTests(unittest.TestCase):
    @staticmethod
    def _sitemap_dates(path: Path) -> dict[str, str]:
        root = ET.parse(path).getroot()
        namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        return {
            entry.findtext("s:loc", namespaces=namespace): entry.findtext(
                "s:lastmod", namespaces=namespace
            )
            for entry in root.findall("s:url", namespace)
        }

    def test_retains_lastmod_only_for_unchanged_page_digests(self) -> None:
        docs = Documentation(version=1, environments=[])
        configuration = {"SM_DOCS_SITE_URL": "https://docs.example.test/"}

        with (
            patch.dict("os.environ", configuration, clear=True),
            tempfile.TemporaryDirectory() as directory,
        ):
            root = Path(directory)
            first_markdown = root / "first-markdown"
            first_html = root / "first-html"
            first_markdown.mkdir()
            (first_markdown / "same.md").write_text("# Same\n", encoding="utf-8")
            (first_markdown / "changed.md").write_text("# Before\n", encoding="utf-8")
            with patch("render_context.datetime") as clock:
                clock.now.return_value.date.return_value.isoformat.return_value = (
                    "2026-01-02"
                )
                HtmlRenderer(docs, first_markdown, first_html)._write_html_tree()

            previous = load_page_digests(first_html / "page-digests.json")
            second_markdown = root / "second-markdown"
            second_html = root / "second-html"
            second_markdown.mkdir()
            (second_markdown / "same.md").write_text("# Same\n", encoding="utf-8")
            (second_markdown / "changed.md").write_text("# After\n", encoding="utf-8")
            with patch("render_context.datetime") as clock:
                clock.now.return_value.date.return_value.isoformat.return_value = (
                    "2026-02-03"
                )
                HtmlRenderer(
                    docs,
                    second_markdown,
                    second_html,
                    previous,
                )._write_html_tree()

            manifest = json.loads((second_html / "page-digests.json").read_text())
            sitemap_dates = self._sitemap_dates(second_html / "sitemap.xml")

        self.assertEqual(manifest["pages"]["same.html"]["lastmod"], "2026-01-02")
        self.assertEqual(manifest["pages"]["changed.html"]["lastmod"], "2026-02-03")
        self.assertEqual(
            sitemap_dates["https://docs.example.test/same.html"], "2026-01-02"
        )
        self.assertEqual(
            sitemap_dates["https://docs.example.test/changed.html"],
            "2026-02-03",
        )


if __name__ == "__main__":
    unittest.main()
