import unittest

from make_ir import parse_blocks


class BlockParsingTests(unittest.TestCase):
    def test_dedents_code_blocks_and_preserves_relative_indentation(self) -> None:
        [block] = parse_blocks(
            [
                "@code",
                "\tfunction example()",
                "\t\treturn true",
                "",
                "\tend",
                "@code",
            ]
        )

        self.assertEqual(
            block["lines"],
            ["function example()", "\treturn true", "", "end"],
        )

    def test_dedents_space_indented_code_blocks(self) -> None:
        [block] = parse_blocks(
            ["@code", "    value = {", "        key = true", "    }", "@code"]
        )

        self.assertEqual(
            block["lines"],
            ["value = {", "    key = true", "}"],
        )


if __name__ == "__main__":
    unittest.main()
