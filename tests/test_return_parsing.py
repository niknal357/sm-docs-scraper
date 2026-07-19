import unittest

from make_ir import _parse_return
from render_markdown import MarkdownRenderer
from symbol_catalog import SymbolCatalog


class ReturnParsingTests(unittest.TestCase):
    def return_parts(self, type_name: str, description: str = "") -> list[str]:
        value = _parse_return(type_name, description)
        return [
            SymbolCatalog.inline_text(part)
            for part in SymbolCatalog.split_inline(value.type)
        ]

    def test_splits_top_level_return_types(self) -> None:
        self.assertEqual(
            self.return_parts("boolean,\t[RaycastResult]", "The result."),
            ["boolean", "RaycastResult"],
        )

    def test_preserves_commas_inside_braces(self) -> None:
        self.assertEqual(
            self.return_parts("{number, number}", "Dimensions."),
            ["{number, number}"],
        )

    def test_extracts_description_embedded_after_tabs(self) -> None:
        value = _parse_return(
            "boolean, integer\t\tTrue if valid; The level.",
            "",
        )
        self.assertEqual(
            [
                SymbolCatalog.inline_text(part)
                for part in SymbolCatalog.split_inline(value.type)
            ],
            ["boolean", "integer"],
        )
        self.assertEqual(
            SymbolCatalog.inline_text(value.description),
            "True if valid; The level.",
        )

    def test_ignores_an_embedded_return_name_column(self) -> None:
        value = _parse_return(
            "[Garage]\t\tGarage\t\tThe Garage object",
            "",
        )
        self.assertEqual(SymbolCatalog.inline_text(value.type), "Garage")
        self.assertEqual(value.name, "Garage")
        self.assertEqual(
            SymbolCatalog.inline_text(value.description),
            "The Garage object",
        )

    def test_ignores_return_name_in_description_column(self) -> None:
        value = _parse_return(
            "boolean",
            "result\t\tReturns true on success.",
        )
        self.assertEqual(value.name, "result")
        self.assertEqual(
            SymbolCatalog.inline_text(value.description),
            "Returns true on success.",
        )

    def test_recognizes_a_return_name_without_description(self) -> None:
        value = _parse_return("[Vec3]", "position")
        self.assertEqual(value.name, "position")
        self.assertEqual(SymbolCatalog.inline_text(value.description), "")

    def test_splits_matching_description_clauses(self) -> None:
        self.assertEqual(
            MarkdownRenderer._return_descriptions(
                "The lift; True if the lift is top",
                2,
            ),
            ["The lift", "True if the lift is top"],
        )

    def test_preserves_shared_descriptions(self) -> None:
        self.assertEqual(
            MarkdownRenderer._return_descriptions(
                "The min and max bounds.", 2
            ),
            ["The min and max bounds."],
        )

    def test_does_not_split_html_entities(self) -> None:
        self.assertEqual(
            MarkdownRenderer._return_descriptions(
                "A fraction from 0&ndash;1; The result",
                2,
            ),
            ["A fraction from 0&ndash;1", "The result"],
        )


if __name__ == "__main__":
    unittest.main()
