import tempfile
import unittest
from pathlib import Path

from make_ir import (
    Doc,
    Documentation,
    Environment,
    Page,
    _normalize_description,
    parse_inline,
)
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

    def test_writes_usage_in_sentence_case(self) -> None:
        page = Page(
            name="sm.test",
            source="test.json",
            usage="server and client",
        )
        environment = Environment(name="Game", namespaces=[page])
        docs = Documentation(version=1, environments=[environment])

        with tempfile.TemporaryDirectory() as directory:
            renderer = MarkdownRenderer(
                docs, Path(directory) / "markdown", Path(directory) / "html"
            )
            renderer._write_page(environment, "namespace", page)
            page_markdown = renderer.page_paths[id(page)].read_text()

        self.assertIn("**Usage:** Server and client", page_markdown)

    def test_writes_descriptive_indexes(self) -> None:
        page = Page(
            name="sm.test",
            source="test.json",
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

            environment_index = (
                markdown_root / "Game-Script-Environment" / "index.md"
            ).read_text()
            category_index = (
                markdown_root
                / "Game-Script-Environment"
                / "Static-Functions"
                / "index.md"
            ).read_text()

        self.assertIn("Browse **1 API page**", environment_index)
        self.assertIn("| Section | Description | Pages |", environment_index)
        self.assertIn("| Page | Description |", category_index)
        self.assertIn("Test helper functions.", category_index)


if __name__ == "__main__":
    unittest.main()
