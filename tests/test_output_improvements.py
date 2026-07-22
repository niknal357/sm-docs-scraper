import tempfile
import unittest
from pathlib import Path

from make_ir import Documentation, Environment, Page, _normalize_description
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


if __name__ == "__main__":
    unittest.main()
