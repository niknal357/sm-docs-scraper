import unittest
from pathlib import Path

from make_ir import Documentation, Environment, Page, parse_inline
from render_markdown import MarkdownRenderer


class ReferenceResolutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cell = Page(name="sm.cell", source="cell.json")
        self.harvestable_namespace = Page(
            name="sm.harvestable",
            source="harvestable-namespace.json",
            associated_type="Harvestable",
        )
        self.effect_namespace = Page(
            name="sm.effect",
            source="effect-namespace.json",
            associated_type="Effect",
        )
        self.terrain_harvestable_namespace = Page(
            name="sm.terrainHarvestable",
            source="terrain-harvestable-namespace.json",
            associated_type="Harvestable",
        )
        self.harvestable = Page(name="Harvestable", source="harvestable.json")
        self.effect = Page(name="Effect", source="effect.json")
        self.environment = Environment(
            name="Game",
            namespaces=[
                self.cell,
                self.harvestable_namespace,
                self.effect_namespace,
                self.terrain_harvestable_namespace,
            ],
            userdata=[self.harvestable, self.effect],
        )
        docs = Documentation(version=1, environments=[self.environment])
        self.renderer = MarkdownRenderer(
            docs,
            Path("markdown"),
            Path("html"),
        )
        self.current_path = self.renderer.page_paths[id(self.cell)]

    def render(self, text: str, *, type_context: bool = False) -> str:
        return self.renderer._inline(
            self.environment,
            self.current_path,
            parse_inline(text),
            type_context=type_context,
        )

    def test_resolves_namespace_reference_in_collection_schema_to_type(self) -> None:
        self.assertEqual(
            self.render(
                "A table {[sm.harvestable, harvestable], ...} of harvestables."
            ),
            "A table {[Harvestable](../Userdata/Harvestable.md), ...} "
            "of harvestables.",
        )

    def test_uses_explicit_namespace_association_instead_of_name_guessing(self) -> None:
        self.assertEqual(
            self.render("{[sm.terrainHarvestable, harvestable], ...}"),
            "{[Harvestable](../Userdata/Harvestable.md), ...}",
        )

    def test_resolves_matching_entity_label_to_type(self) -> None:
        self.assertEqual(
            self.render("Attached to a [sm.harvestable, harvestable]."),
            "Attached to a [Harvestable](../Userdata/Harvestable.md).",
        )
        self.assertEqual(
            self.render("Returns a table of [sm.harvestable, harvestables]."),
            "Returns a table of [Harvestables](../Userdata/Harvestable.md).",
        )

    def test_resolves_namespace_reference_in_declared_type_context(self) -> None:
        self.assertEqual(
            self.render("[sm.harvestable]", type_context=True),
            "[Harvestable](../Userdata/Harvestable.md)",
        )

    def test_capitalizes_irregular_plural_type_labels(self) -> None:
        self.assertEqual(
            self.renderer._associated_type_link_label(
                "Body", "bodies", explicit_label=True
            ),
            "Bodies",
        )

    def test_preserves_namespace_links_in_api_context(self) -> None:
        self.assertEqual(
            self.render("See the [sm.effect, effect] API."),
            "See the [effect](sm.effect.md) API.",
        )
        self.assertEqual(
            self.render("For details, see [sm.effect, effect]."),
            "For details, see [effect](sm.effect.md).",
        )
        self.assertEqual(
            self.render("For details, see [sm.effect]."),
            "For details, see [sm.effect](sm.effect.md).",
        )

    def test_preserves_custom_label_that_does_not_name_the_type(self) -> None:
        self.assertEqual(
            self.render("Read the [sm.effect, effects guide]."),
            "Read the [effects guide](sm.effect.md).",
        )


if __name__ == "__main__":
    unittest.main()
