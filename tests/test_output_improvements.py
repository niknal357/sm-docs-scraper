import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urljoin

from make_ir import (
    Doc,
    Documentation,
    Entry,
    Environment,
    Page,
    Parameter,
    ReturnValue,
    _normalize_description,
    parse_inline,
)
from render_html import HtmlRenderer
from render_markdown import MarkdownRenderer


class OutputImprovementTests(unittest.TestCase):
    def test_corrects_malformed_destruction_type_reference(self) -> None:
        description = _normalize_description(
            "The type of destruction. (See[sm.shape.destructionType)."
        )
        self.assertEqual(
            description,
            "The type of destruction. (See [sm.shape.destructionType]).",
        )

    def test_writes_descriptive_indexes_and_sentence_case_usage(self) -> None:
        page = Page(
            name="sm.test",
            source="test.json",
            usage="server and client",
            doc=Doc(
                content=[
                    {
                        "type": "paragraph",
                        "content": parse_inline("Test helper functions."),
                    }
                ]
            ),
        )
        environment = Environment(name="Game", namespaces=[page])
        docs = Documentation(version=1, environments=[environment])

        with tempfile.TemporaryDirectory() as directory:
            markdown_root = Path(directory) / "markdown"
            renderer = MarkdownRenderer(
                docs, markdown_root, Path(directory) / "html"
            )
            renderer._write_environment_index(environment)
            renderer._write_category_index(environment, "namespace", [page])
            renderer._write_page(environment, "namespace", page)

            environment_index = (
                markdown_root / "Game-Script-Environment" / "index.md"
            ).read_text()
            category_index = (
                markdown_root
                / "Game-Script-Environment"
                / "Static-Functions"
                / "index.md"
            ).read_text()
            page_markdown = renderer.page_paths[id(page)].read_text()

        self.assertIn("Browse **1 API page**", environment_index)
        self.assertIn("| Section | Description | Pages |", environment_index)
        self.assertIn("| Page | Description |", category_index)
        self.assertIn("Test helper functions.", category_index)
        self.assertIn("**Usage:** Server and client", page_markdown)

    def test_preserves_braced_schemas_in_html_tables(self) -> None:
        page = Page(
            name="sm.test",
            source="test.json",
            functions=[
                Entry(
                    name="inspect",
                    doc=Doc(
                        parameters=[
                            Parameter(
                                name="schema",
                                type=["table"],
                                description=parse_inline(
                                    "Grid data {type=string, count=integer}"
                                ),
                            )
                        ],
                        returns=[
                            ReturnValue(
                                type=["table"],
                                description=parse_inline(
                                    "The table of { min, max }"
                                ),
                            )
                        ],
                    ),
                )
            ],
        )
        environment = Environment(name="Game", namespaces=[page])
        docs = Documentation(version=1, environments=[environment])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            markdown_root = root / "markdown"
            html_root = root / "html"
            markdown_renderer = MarkdownRenderer(docs, markdown_root, html_root)
            markdown_renderer._write_page(environment, "namespace", page)
            HtmlRenderer(docs, markdown_root, html_root)._write_html_tree()

            markdown_path = markdown_renderer.page_paths[id(page)]
            markdown_output = markdown_path.read_text()
            html_path = html_root / markdown_path.relative_to(
                markdown_root
            ).with_suffix(".html")
            html_output = html_path.read_text()

        self.assertIn(r"Grid data \{type=string, count=integer\}", markdown_output)
        self.assertIn(r"The table of \{ min, max \}", markdown_output)
        self.assertIn("Grid data {type=string, count=integer}", html_output)
        self.assertIn("The table of { min, max }", html_output)
        self.assertNotIn('<td count="integer"', html_output)
        self.assertNotIn('<td max="max"', html_output)

    def test_merges_member_parameter_and_return_details(self) -> None:
        page = Page(
            name="Sample",
            source="sample.json",
            members=[
                Entry(
                    name="payload",
                    get=Doc(
                        content=[
                            {
                                "type": "paragraph",
                                "content": parse_inline("Returns the payload."),
                            }
                        ],
                        parameters=[
                            Parameter(
                                name="sample",
                                type=parse_inline("[Sample]"),
                                description=parse_inline("The sample."),
                            )
                        ],
                        returns=[
                            ReturnValue(
                                type=["table"],
                                description=parse_inline(
                                    "Includes the complete payload metadata."
                                ),
                            )
                        ],
                    ),
                    set=Doc(
                        content=[
                            {
                                "type": "paragraph",
                                "content": parse_inline(
                                    "Sets the cached payload."
                                ),
                            }
                        ],
                        parameters=[
                            Parameter(
                                name="sample",
                                type=parse_inline("[Sample]"),
                                description=parse_inline("The sample."),
                            ),
                            Parameter(
                                name="value",
                                type=["table"],
                                description=parse_inline(
                                    "Must include the payload metadata."
                                ),
                            ),
                        ],
                    ),
                ),
                Entry(
                    name="fraction",
                    get=Doc(
                        content=[
                            {
                                "type": "paragraph",
                                "content": parse_inline(
                                    "Returns the fraction of the distance."
                                ),
                            }
                        ],
                        returns=[
                            ReturnValue(
                                type=["number"],
                                description=parse_inline(
                                    "The fraction of the distance."
                                ),
                            )
                        ],
                    ),
                ),
            ],
        )
        environment = Environment(name="Game", userdata=[page])
        docs = Documentation(version=1, environments=[environment])

        with tempfile.TemporaryDirectory() as directory:
            markdown_root = Path(directory) / "markdown"
            renderer = MarkdownRenderer(
                docs, markdown_root, Path(directory) / "html"
            )
            renderer._write_page(environment, "userdata", page)
            output = renderer.page_paths[id(page)].read_text()

        self.assertIn(
            "`Get`: Includes the complete payload metadata.", output
        )
        self.assertIn(
            "`Set`: Sets the cached payload. <br> "
            "**Value:** Must include the payload metadata.",
            output,
        )
        self.assertEqual(output.count("fraction of the distance"), 1)
        self.assertNotIn("**Result:** The fraction", output)
        self.assertNotIn("**Returns:** [ **table** ]", output)

    def test_adds_api_page_presentation_hooks(self) -> None:
        body = """<h1 id="sample">Sample</h1>
<p><strong>Associated namespace:</strong> <a href="sm.sample.md">sm.sample</a></p>
<p><strong>Usage:</strong> Server and client</p>
<p><strong>Serializable:</strong> Yes</p>
<p>Sample description.</p>
<p><strong>Values:</strong></p>
<ul><li><code>value</code><ul><li><code>Get</code>: A value.</li></ul></li></ul>
<h2 id="methods">Methods</h2>
<h3 id="inspect">inspect</h3>
<div class="api-signature codehilite"><pre><code>sample:inspect()</code></pre></div>"""

        body = HtmlRenderer._render_api_metadata(body)
        body = HtmlRenderer._render_member_values(body)

        self.assertIn('<dl class="api-metadata">', body)
        self.assertLess(body.index("Availability"), body.index("Serializable"))
        self.assertLess(body.index("Serializable"), body.index("Associated namespace"))
        self.assertIn("<dd>Server + Client</dd>", body)
        self.assertIn('class="api-members-heading"', body)
        self.assertIn('href="#inspect"', HtmlRenderer._table_of_contents(body))

    def test_omits_empty_table_of_contents_and_expands_layout(self) -> None:
        docs = Documentation(version=1, environments=[])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            markdown_root = root / "markdown"
            markdown_root.mkdir()
            (markdown_root / "plain.md").write_text("# Plain\n")
            (markdown_root / "sections.md").write_text(
                "# Sections\n\n## Details\n"
            )

            renderer = HtmlRenderer(docs, markdown_root, root / "html")
            renderer._write_html_tree()
            plain_html = (root / "html" / "plain.html").read_text()
            sections_html = (root / "html" / "sections.html").read_text()
            logo_exists = (root / "html" / "assets" / "logo.png").is_file()

        self.assertIn('class="content-layout without-toc"', plain_html)
        self.assertNotIn('class="table-of-contents"', plain_html)
        self.assertIn('src="assets/logo.png"', plain_html)
        self.assertIn('rel="icon" type="image/png" href="assets/logo.png"', plain_html)
        self.assertTrue(logo_exists)
        self.assertIn('class="content-layout"', sections_html)
        self.assertIn('class="table-of-contents"', sections_html)

    def test_marks_pages_without_published_api_content(self) -> None:
        page = Page(name="sm.empty", source="empty.json", doc=Doc())
        environment = Environment(name="Game", namespaces=[page])
        docs = Documentation(version=1, environments=[environment])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            renderer = MarkdownRenderer(docs, root / "markdown", root / "html")
            renderer._write_page(environment, "namespace", page)
            renderer._write_category_index(environment, "namespace", [page])
            page_output = renderer.page_paths[id(page)].read_text()
            index_output = (
                root
                / "markdown"
                / "Game-Script-Environment"
                / "Static-Functions"
                / "index.md"
            ).read_text()

        self.assertIn("This is intentional, not a rendering error", page_output)
        self.assertIn("published Scrap Mechanic API data", page_output)
        self.assertIn(
            "No description or API members are present in the published source.",
            index_output,
        )

    def test_separates_deprecated_member_accessors(self) -> None:
        deprecation = [
            {"type": "paragraph", "content": parse_inline("Use [Sample].")}
        ]
        member = Entry(
            name="value",
            get=Doc(
                content=[
                    {"type": "paragraph", "content": parse_inline("Removed!")}
                ],
                deprecated=deprecation,
            ),
            set=Doc(
                content=[
                    {"type": "paragraph", "content": parse_inline("Removed!")}
                ],
                deprecated=deprecation,
            ),
        )
        page = Page(name="Sample", source="sample.json", members=[member])
        environment = Environment(name="Game", userdata=[page])
        docs = Documentation(version=1, environments=[environment])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            markdown_root = root / "markdown"
            MarkdownRenderer(docs, markdown_root, root / "html")._write_page(
                environment, "userdata", page
            )
            HtmlRenderer(docs, markdown_root, root / "html")._write_html_tree()
            output = (
                root
                / "html"
                / "Game-Script-Environment"
                / "Userdata"
                / "Sample.html"
            ).read_text()

        self.assertEqual(output.count("<code>Set</code>: Removed!"), 1)
        self.assertNotIn("    - <code>Set</code>", output)

    def test_writes_seo_and_static_host_files(self) -> None:
        docs = Documentation(version=1, environments=[])
        configuration = {
            "SM_DOCS_SITE_URL": "https://docs.example.test/",
        }

        with (
            patch.dict(os.environ, configuration, clear=True),
            tempfile.TemporaryDirectory() as directory,
        ):
            root = Path(directory)
            markdown_root = root / "markdown"
            markdown_root.mkdir()
            with patch("render_context.datetime") as clock:
                clock.now.return_value.date.return_value.isoformat.return_value = (
                    "2026-07-24"
                )
                renderer = MarkdownRenderer(docs, markdown_root, root / "html")
                renderer._write_markdown_index()
                renderer._write_search_page()
                renderer._write_not_found_page()
                HtmlRenderer(docs, markdown_root, root / "html")._write_html_tree()

            html_root = root / "html"
            introduction = (markdown_root / "index.md").read_text()
            index_html = (html_root / "index.html").read_text()
            search_html = (html_root / "search.html").read_text()
            not_found_html = (html_root / "404.html").read_text()
            sitemap = (html_root / "sitemap.xml").read_text()
            robots = (html_root / "robots.txt").read_text()

            self.assertFalse((html_root / "CNAME").exists())
            self.assertTrue((html_root / ".nojekyll").is_file())

        self.assertIn("Site build date:** 2026-07-24 UTC", introduction)
        self.assertNotIn("Target game version", introduction)
        self.assertIn('<meta name="description"', index_html)
        self.assertIn(
            '<link rel="canonical" href="https://docs.example.test/">',
            index_html,
        )
        self.assertIn('<meta property="og:title"', index_html)
        self.assertIn('href="#main-content">Skip to main content</a>', index_html)
        self.assertIn('<meta name="robots" content="noindex,follow">', search_html)
        self.assertNotIn("<base ", not_found_html)
        self.assertIn('href="#main-content">Skip to main content</a>', not_found_html)
        self.assertIn('href="/index.html"', not_found_html)
        self.assertIn('data-symbol-index="/assets/search-symbols.json"', not_found_html)
        self.assertNotIn('rel="canonical"', not_found_html)
        self.assertIn("https://docs.example.test/", sitemap)
        self.assertNotIn("search.html", sitemap)
        self.assertNotIn("404.html", sitemap)
        self.assertIn(
            "Sitemap: https://docs.example.test/sitemap.xml", robots
        )

    def test_writes_portable_not_found_urls(self) -> None:
        docs = Documentation(version=1, environments=[])
        configuration = {
            "SM_DOCS_SITE_URL": "https://owner.github.io/repo",
        }

        with (
            patch.dict(os.environ, configuration, clear=True),
            tempfile.TemporaryDirectory() as directory,
        ):
            root = Path(directory)
            markdown_root = root / "markdown"
            markdown_root.mkdir()
            renderer = MarkdownRenderer(docs, markdown_root, root / "html")
            renderer._write_markdown_index()
            renderer._write_search_page()
            renderer._write_not_found_page()
            HtmlRenderer(docs, markdown_root, root / "html")._write_html_tree()

            html_root = root / "html"
            index_html = (html_root / "index.html").read_text()
            not_found_html = (html_root / "404.html").read_text()
            cname_exists = (html_root / "CNAME").exists()

        self.assertFalse(cname_exists)
        self.assertIn(
            '<link rel="canonical" href="https://owner.github.io/repo/">',
            index_html,
        )
        self.assertNotIn("<base ", not_found_html)
        self.assertIn('href="#main-content">Skip to main content</a>', not_found_html)
        self.assertIn('href="/repo/index.html"', not_found_html)
        self.assertIn(
            'data-symbol-index="/repo/assets/search-symbols.json"',
            not_found_html,
        )
        self.assertEqual(
            urljoin(
                "https://owner.github.io/repo/old/nested/page",
                "/repo/assets/search-symbols.json",
            ),
            "https://owner.github.io/repo/assets/search-symbols.json",
        )

    def test_rejects_invalid_public_build_configuration(self) -> None:
        docs = Documentation(version=1, environments=[])
        invalid_site_urls = (
            "https://example.test/docs?preview=1",
            "https://example.test/docs#preview",
            "https://user:password@example.test/docs",
        )
        for site_url in invalid_site_urls:
            with (
                self.subTest(site_url=site_url),
                patch.dict(
                    os.environ,
                    {"SM_DOCS_SITE_URL": site_url},
                    clear=True,
                ),
                self.assertRaisesRegex(ValueError, "SM_DOCS_SITE_URL"),
            ):
                MarkdownRenderer(docs, Path("markdown"), Path("html"))

    def test_distinguishes_environment_titles(self) -> None:
        game_page = Page(name="Color", source="game.json", doc=Doc())
        terrain_page = Page(name="Color", source="terrain.json", doc=Doc())
        game = Environment(name="Game", userdata=[game_page])
        terrain = Environment(name="Terrain", userdata=[terrain_page])
        docs = Documentation(version=1, environments=[game, terrain])

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            markdown_root = root / "markdown"
            renderer = MarkdownRenderer(docs, markdown_root, root / "html")
            renderer._write_page(game, "userdata", game_page)
            renderer._write_page(terrain, "userdata", terrain_page)
            HtmlRenderer(docs, markdown_root, root / "html")._write_html_tree()
            game_html = (
                root
                / "html"
                / "Game-Script-Environment"
                / "Userdata"
                / "Color.html"
            ).read_text()
            terrain_html = (
                root
                / "html"
                / "Terrain-Script-Environment"
                / "Userdata"
                / "Color.html"
            ).read_text()

        self.assertIn("<title>Color — Game API | SM Docs</title>", game_html)
        self.assertIn("<title>Color — Terrain API | SM Docs</title>", terrain_html)


if __name__ == "__main__":
    unittest.main()
