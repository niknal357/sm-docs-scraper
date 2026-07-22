import json
import tempfile
import unittest
from pathlib import Path

from make_ir import Doc, Documentation, Entry, Environment, Page, parse_inline
from search_index import LINK_PREVIEW_INDEX_NAME, write_link_preview_index
from symbol_catalog import SymbolCatalog


class LinkPreviewTests(unittest.TestCase):
    def test_writes_preview_details_for_pages_and_functions(self) -> None:
        function = Entry(
            name="test",
            doc=Doc(
                content=[
                    {
                        "type": "paragraph",
                        "content": parse_inline("Returns a <strong>test</strong> value."),
                    }
                ]
            ),
        )
        page = Page(
            name="sm.example",
            source="test.json",
            doc=Doc(
                content=[
                    {
                        "type": "paragraph",
                        "content": parse_inline("Example helpers."),
                    }
                ]
            ),
            functions=[function],
        )
        docs = Documentation(
            version=1,
            environments=[Environment(name="Game", namespaces=[page])],
        )

        with tempfile.TemporaryDirectory() as directory:
            html_root = Path(directory)
            (html_root / "assets").mkdir()
            output = write_link_preview_index(SymbolCatalog(docs), html_root)
            payload = json.loads(output.read_text())

        self.assertEqual(output.name, LINK_PREVIEW_INDEX_NAME)
        self.assertEqual(payload["version"], 1)
        records = {record["url"]: record for record in payload["records"]}
        page_url = "Game-Script-Environment/Static-Functions/sm.example.html"
        function_record = records[f"{page_url}#test"]
        self.assertEqual(records[page_url]["summary"], "Example helpers.")
        self.assertEqual(function_record["title"], "sm.example.test")
        self.assertEqual(
            function_record["hierarchy"],
            "Game › Static Functions › sm.example",
        )
        self.assertEqual(function_record["signature"], "sm.example.test(  )")
        self.assertEqual(function_record["summary"], "Returns a test value.")


if __name__ == "__main__":
    unittest.main()
