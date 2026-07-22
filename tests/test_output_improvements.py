import tempfile
import unittest
from pathlib import Path

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

        self.assertIn('class="content-layout without-toc"', plain_html)
        self.assertNotIn('class="table-of-contents"', plain_html)
        self.assertIn('class="content-layout"', sections_html)
        self.assertIn('class="table-of-contents"', sections_html)


if __name__ == "__main__":
    unittest.main()
