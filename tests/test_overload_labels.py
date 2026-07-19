import unittest

from make_ir import (
    Doc,
    Documentation,
    Entry,
    Environment,
    Page,
    Parameter,
    parse_inline,
)
from symbol_catalog import PRIMITIVE_TYPES, SymbolCatalog


class OverloadLabelTests(unittest.TestCase):
    @staticmethod
    def parameter(
        name: str, type_name: str, optional: bool = False
    ) -> Parameter:
        raw_type = (
            type_name
            if type_name.casefold() in PRIMITIVE_TYPES
            else f"[{type_name}]"
        )
        return Parameter(
            name=name,
            type=parse_inline(raw_type),
            description=[],
            optional=optional,
        )

    def labels(
        self, name: str, signatures: list[list[Parameter]]
    ) -> tuple[list[str], list[str]]:
        entries = [Entry(name=name, doc=Doc(parameters=parameters)) for parameters in signatures]
        page = Page(name="sm.test", source="test.json", functions=entries)
        docs = Documentation(
            version=1,
            environments=[Environment(name="Game", namespaces=[page])],
        )
        catalog = SymbolCatalog(docs)
        anchors = [catalog.method_anchor(page, entry) for entry in entries]
        return (
            [anchor.label for anchor in anchors],
            [anchor.anchor for anchor in anchors],
        )

    def test_uses_one_differing_userdata_type(self) -> None:
        labels, anchors = self.labels(
            "applyImpulse",
            [
                [
                    self.parameter("target", "Shape"),
                    self.parameter("impulse", "Vec3"),
                ],
                [
                    self.parameter("target", "Body"),
                    self.parameter("impulse", "Vec3"),
                ],
                [
                    self.parameter("target", "Character"),
                    self.parameter("impulse", "Vec3"),
                ],
            ],
        )
        self.assertEqual(
            labels,
            [
                "applyImpulse - Shape",
                "applyImpulse - Body",
                "applyImpulse - Character",
            ],
        )
        self.assertEqual(
            anchors,
            [
                "applyimpulse-shape-vec3",
                "applyimpulse-body-vec3",
                "applyimpulse-character-vec3",
            ],
        )

    def test_uses_multiple_independent_discriminators(self) -> None:
        labels, _ = self.labels(
            "meleeAttack",
            [
                [self.parameter("name", "string"), self.parameter("source", "Player")],
                [self.parameter("name", "string"), self.parameter("source", "Unit")],
                [self.parameter("uuid", "Uuid"), self.parameter("source", "Player")],
                [self.parameter("uuid", "Uuid"), self.parameter("source", "Unit")],
            ],
        )
        self.assertEqual(
            labels,
            [
                "meleeAttack - name + Player",
                "meleeAttack - name + Unit",
                "meleeAttack - Uuid + Player",
                "meleeAttack - Uuid + Unit",
            ],
        )

    def test_aligns_shifted_parameters_by_name(self) -> None:
        labels, _ = self.labels(
            "compassSetIconHost",
            [
                [
                    self.parameter("host", "Character"),
                    self.parameter("joint", "string", optional=True),
                ],
                [
                    self.parameter("iconName", "string"),
                    self.parameter("host", "Shape"),
                    self.parameter("joint", "string", optional=True),
                ],
            ],
        )
        self.assertEqual(
            labels,
            [
                "compassSetIconHost - Character",
                "compassSetIconHost - Shape",
            ],
        )

    def test_describes_a_missing_discriminator_by_argument_count(self) -> None:
        labels, _ = self.labels(
            "createEffect",
            [
                [self.parameter("name", "string")],
                [
                    self.parameter("name", "string"),
                    self.parameter("host", "Interactable"),
                ],
                [
                    self.parameter("name", "string"),
                    self.parameter("host", "Shape"),
                ],
            ],
        )
        self.assertEqual(
            labels,
            [
                "createEffect - 1 argument",
                "createEffect - Interactable",
                "createEffect - Shape",
            ],
        )

    def test_uses_meaningful_primitive_parameter_names(self) -> None:
        labels, _ = self.labels(
            "createBlueprint",
            [
                [self.parameter("path", "string")],
                [self.parameter("blueprintTable", "table")],
            ],
        )
        self.assertEqual(
            labels,
            [
                "createBlueprint - path",
                "createBlueprint - blueprintTable",
            ],
        )

    def test_falls_back_for_short_or_colliding_primitive_names(self) -> None:
        color_labels, _ = self.labels(
            "new",
            [
                [self.parameter("color", "Color")],
                [
                    self.parameter("r", "number"),
                    self.parameter("g", "number"),
                    self.parameter("b", "number"),
                ],
                [self.parameter("hexStr", "string")],
                [self.parameter("hexInt", "integer")],
            ],
        )
        self.assertEqual(
            color_labels,
            ["new - Color", "new - number", "new - hexStr", "new - hexInt"],
        )

        uuid_labels, _ = self.labels(
            "new",
            [
                [self.parameter("uuid", "Uuid", optional=True)],
                [self.parameter("uuid", "string", optional=True)],
            ],
        )
        self.assertEqual(uuid_labels, ["new - Uuid", "new - string"])


if __name__ == "__main__":
    unittest.main()
