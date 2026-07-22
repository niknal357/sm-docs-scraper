from __future__ import annotations

from html import unescape
import json
import os
from pathlib import Path
import re

from make_ir import Doc, Entry, Environment, Inline, Page
from render_context import CATEGORY_DIRECTORIES, CATEGORY_TITLES, RenderContext
from symbol_catalog import CallbackGroup, SIGNATURE_LINE_LENGTH, SymbolCatalog


SIGNATURE_FENCE = "``` { .lua .api-signature }"
INTRODUCTION_PATH = Path(__file__).parent / "content" / "introduction.md"
SEARCH_PATH = Path(__file__).parent / "content" / "search.md"
LEGACY_EMPTY_LINK = re.compile(
    r'<a href="index\.html#(?:server|client|console)">(.*?)</a>',
    flags=re.IGNORECASE,
)
LUA_LITERAL = re.compile(
    r"(?:-?(?:\d+(?:\.\d*)?|\.\d+)|true|false|nil|"
    r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')'
)


class MarkdownRenderer(RenderContext):
    def _inline(
        self, environment: Environment, current_path: Path, content: Inline
    ) -> str:
        rendered = []
        for part in content:
            if isinstance(part, str):
                rendered.append(LEGACY_EMPTY_LINK.sub(r"\1", part))
                continue
            target = part["reference"]
            label = part.get("label", target)
            rendered.append(self._link(environment, current_path, target, label))
        return "".join(rendered)

    def _blocks(
        self,
        environment: Environment,
        current_path: Path,
        blocks: list[dict],
        tables_as_lua: bool = False,
    ) -> list[str]:
        output: list[str] = []
        for block in blocks:
            block_type = block["type"]
            if block_type == "paragraph":
                output.extend(
                    [self._inline(environment, current_path, block["content"]), ""]
                )
            elif block_type == "code":
                output.extend(
                    [
                        f"```{block.get('language', '')}",
                        *block["lines"],
                        "```",
                        "",
                    ]
                )
            elif block_type == "list":
                output.extend(
                    f"- {self._inline(environment, current_path, item)}"
                    for item in block["items"]
                )
                output.append("")
            elif block_type == "table":
                if tables_as_lua:
                    output.extend(self._lua_table_block(block["rows"]))
                else:
                    output.extend(
                        self._table_block(environment, current_path, block["rows"])
                    )
            elif block_type in {"note", "warning"}:
                label = block_type.title()
                output.append(f"> **{label}:**")
                for line in block["content"]:
                    output.append(
                        f"> {self._inline(environment, current_path, line)}"
                    )
                output.append("")
        return output

    def _lua_table_block(self, rows: list[list[Inline]]) -> list[str]:
        values = [
            [
                unescape(
                    re.sub(r"<[^>]+>", "", self.symbol_catalog.inline_text(cell))
                ).strip()
                for cell in row
            ]
            for row in rows
        ]
        mappings = bool(values) and all(
            len(row) == 2 and LUA_LITERAL.fullmatch(row[1]) for row in values
        )

        lines = ["```lua", "{"]
        if mappings:
            width = max(len(row[0]) for row in values)
            lines.extend(
                f"    {key:<{width}} = {value}," for key, value in values
            )
        else:
            width = max((len(row[0].rstrip(",")) for row in values), default=0)
            for row in values:
                value = row[0].rstrip(",")
                line = f"    {value},"
                if len(row) > 1:
                    description = " | ".join(row[1:])
                    line = f"    {value + ',':<{width + 1}} -- {description}"
                lines.append(line)
        lines.extend(["}", "```", ""])
        return lines

    def _table_block(
        self,
        environment: Environment,
        current_path: Path,
        rows: list[list[Inline]],
    ) -> list[str]:
        width = max((len(row) for row in rows), default=1)
        headers = {
            1: ["Value"],
            2: ["Value", "Description"],
            3: ["Type", "Name", "Description"],
        }.get(width, [f"Column {number}" for number in range(1, width + 1)])

        output = [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join("---" for _ in headers) + " |",
        ]
        for row in rows:
            cells = [
                self._inline(environment, current_path, cell).replace("|", "\\|")
                for cell in row
            ]
            cells.extend([""] * (width - len(cells)))
            output.append("| " + " | ".join(cells) + " |")
        output.append("")
        return output

    @staticmethod
    def _return_descriptions(description: str, type_count: int) -> list[str]:
        parts = re.split(r";\s+", description)
        if type_count > 1 and len(parts) == type_count:
            return parts
        return [description]

    def _doc(
        self,
        environment: Environment,
        current_path: Path,
        doc: Doc,
        detail_heading: int,
        show_availability: bool = True,
        show_returns: bool = True,
        tables_as_lua: bool = False,
    ) -> list[str]:
        output: list[str] = []

        if doc.hidden:
            output.extend(["**Visibility:** Hidden", ""])
        if show_availability and doc.availability != "server and client":
            output.extend([f"**Availability:** {doc.availability.title()} only", ""])
        if doc.deprecated:
            output.extend(["> **Deprecated:**", *self._quote_blocks(environment, current_path, doc.deprecated), ""])

        output.extend(
            self._blocks(
                environment,
                current_path,
                doc.content,
                tables_as_lua=tables_as_lua,
            )
        )
        heading = "#" * detail_heading

        if doc.fields:
            output.extend([f"{heading} Fields", ""])
            rows = []
            for item in doc.fields:
                rows.append(
                    [
                        f"`{item.name}`",
                        self._inline(environment, current_path, item.type),
                        self._inline(environment, current_path, item.description),
                    ]
                )
            output.extend(self._plain_table(["Name", "Type", "Description"], rows))

        if doc.operations:
            output.extend([f"{heading} Operations", ""])
            rows = [
                [
                    self._inline(environment, current_path, item.signature),
                    self._inline(environment, current_path, item.description),
                ]
                for item in doc.operations
            ]
            output.extend(self._plain_table(["Signature", "Description"], rows))

        if doc.parameters:
            output.extend(["**Parameters:**", ""])
            rows = []
            for parameter in doc.parameters:
                name = f"`{parameter.name}`"
                if parameter.optional:
                    name += " *(optional)*"
                rows.append(
                    [
                        name,
                        self._inline(environment, current_path, parameter.type),
                        self._inline(environment, current_path, parameter.description),
                    ]
                )
            output.extend(self._plain_table(["Name", "Type", "Description"], rows))

        if show_returns and doc.returns:
            output.extend(["**Returns:**", ""])
            show_names = any(item.name for item in doc.returns)
            rows = []
            for item in doc.returns:
                type_names = [
                    self._inline(environment, current_path, type_name)
                    for type_name in self.symbol_catalog.split_inline(item.type)
                ]
                description = self._inline(
                    environment, current_path, item.description
                )
                descriptions = self._return_descriptions(
                    description, len(type_names)
                )
                if len(descriptions) == len(type_names):
                    item_rows = [
                        [type_name, return_description]
                        for type_name, return_description in zip(
                            type_names, descriptions, strict=True
                        )
                    ]
                else:
                    item_rows = [["<br>".join(type_names), description]]

                if show_names:
                    for index, row in enumerate(item_rows):
                        name = f"`{item.name}`" if index == 0 and item.name else ""
                        row.insert(0, name)
                rows.extend(item_rows)

            headers = (
                ["Name", "Type", "Description"]
                if show_names
                else ["Type", "Description"]
            )
            output.extend(self._plain_table(headers, rows))

        return output

    def _quote_blocks(
        self,
        environment: Environment,
        current_path: Path,
        blocks: list[dict],
    ) -> list[str]:
        quoted = []
        for line in self._blocks(environment, current_path, blocks):
            quoted.append(f"> {line}" if line else ">")
        return quoted

    @staticmethod
    def _plain_table(headers: list[str], rows: list[list[str]]) -> list[str]:
        output = [
            "| " + " | ".join(headers) + " |",
            "| " + " | ".join("---" for _ in headers) + " |",
        ]
        for row in rows:
            cells = [
                (cell or "&mdash;").replace("|", "\\|")
                for cell in row
            ]
            output.append("| " + " | ".join(cells) + " |")
        output.append("")
        return output

    def _operations(
        self,
        environment: Environment,
        current_path: Path,
        entries: list[Entry],
    ) -> list[str]:
        if not entries:
            return []

        rows = []
        for entry in entries:
            if entry.doc is None or not entry.doc.operations:
                raise ValueError(f"Missing operation metadata: {entry.name}")
            for index, operation in enumerate(entry.doc.operations):
                expression, result = self.symbol_catalog.operation_signature(
                    entry.name, operation.signature
                )
                anchor = (
                    f'<a id="{self.symbol_catalog.slug(entry.name)}"></a>'
                    if index == 0
                    else ""
                )
                rows.append(
                    [
                        f"{anchor}`{expression}`",
                        self._inline(environment, current_path, result),
                        self._inline(environment, current_path, operation.description),
                    ]
                )

        return [
            "**Operations:**",
            "",
            *self._plain_table(["Operation", "Returns", "Description"], rows),
        ]

    def _callback_aliases(self, callback: CallbackGroup) -> list[str]:
        return [
            f'<a id="{self.symbol_catalog.slug(entry.name)}"></a>'
            for entry in (callback.server, callback.client)
            if entry
        ]

    def _callback_entry(
        self,
        environment: Environment,
        current_path: Path,
        page: Page,
        callback: CallbackGroup,
    ) -> list[str]:
        anchor = self.symbol_catalog.slug(callback.name)
        output = [
            *self._callback_aliases(callback),
            f"### {callback.name} {{#{anchor}}}",
            "",
        ]
        server = callback.server
        client = callback.client

        if server and client and server.doc == client.doc:
            output.extend(
                [
                    SIGNATURE_FENCE,
                    self.symbol_catalog.signature(page, server),
                    self.symbol_catalog.signature(page, client),
                    "```",
                    "",
                ]
            )
            if server.doc:
                output.extend(self._doc(environment, current_path, server.doc, 4))
            return output

        entries = (("Server", server), ("Client", client))
        paired = server is not None and client is not None
        for side, entry in entries:
            if entry is None:
                continue
            if paired:
                output.extend([f"#### {side}", ""])
            output.extend(
                [
                    SIGNATURE_FENCE,
                    self.symbol_catalog.signature(page, entry),
                    "```",
                    "",
                ]
            )
            if entry.doc:
                detail_heading = 5 if paired else 4
                output.extend(
                    self._doc(environment, current_path, entry.doc, detail_heading)
                )
        return output

    def _callbacks(
        self,
        environment: Environment,
        current_path: Path,
        page: Page,
    ) -> list[str]:
        groups = self.symbol_catalog.callback_groups(page)
        categories = (
            (
                "Server + Client",
                [callback for callback in groups if callback.server and callback.client],
            ),
            (
                "Server-only",
                [callback for callback in groups if callback.server and not callback.client],
            ),
            (
                "Client-only",
                [callback for callback in groups if callback.client and not callback.server],
            ),
        )

        output: list[str] = []
        for title, callbacks in categories:
            if not callbacks:
                continue
            output.extend([f"## {title}", ""])
            for callback in callbacks:
                output.extend(
                    self._callback_entry(
                        environment, current_path, page, callback
                    )
                )
        return output

    def _methods(
        self,
        environment: Environment,
        current_path: Path,
        kind: str,
        page: Page,
    ) -> list[str]:
        availability_categories = (
            ("server and client", "Server + Client"),
            ("server", "Server-only"),
            ("client", "Client-only"),
        )
        known_availability = {
            availability for availability, _ in availability_categories
        }
        unknown = [
            entry.name
            for entry in page.functions
            if entry.doc is None or entry.doc.availability not in known_availability
        ]
        if unknown:
            raise ValueError(
                f"Unknown method availability on {page.name}: {', '.join(unknown)}"
            )

        availability = {
            entry.doc.availability for entry in page.functions if entry.doc
        }
        categories = (
            (("server and client", "Functions"),)
            if availability == {"server and client"}
            else availability_categories
        )

        output: list[str] = []
        method_anchors = self.symbol_catalog.method_anchors(page)
        for availability, title in categories:
            entries = [
                entry
                for entry in page.functions
                if entry.doc and entry.doc.availability == availability
            ]
            if not entries:
                continue

            output.extend([f"## {title}", ""])
            for entry in entries:
                method_anchor = method_anchors[id(entry)]
                if method_anchor.legacy_alias:
                    output.append(f'<a id="{method_anchor.legacy_alias}"></a>')
                output.extend(
                    [
                        f"### {method_anchor.label} {{#{method_anchor.anchor}}}",
                        "",
                        SIGNATURE_FENCE,
                        self.symbol_catalog.signature(page, entry),
                        "```",
                        "",
                    ]
                )
                output.extend(
                    self._doc(
                        environment,
                        current_path,
                        entry.doc,
                        4,
                        show_availability=False,
                    )
                )
        return output

    @staticmethod
    def _constant_values_missing(entry: Entry) -> bool:
        doc = entry.doc
        if doc is None:
            return False
        is_table = any(
            SymbolCatalog.inline_text(value.type).casefold() == "table"
            for value in doc.returns
        )
        has_values = any(
            block["type"] in {"code", "list", "table"} for block in doc.content
        )
        return is_table and not has_values

    @classmethod
    def _constant_has_details(cls, entry: Entry) -> bool:
        doc = entry.doc
        if doc is None:
            return False
        return bool(
            cls._constant_values_missing(entry)
            or len(doc.content) > 1
            or any(block["type"] != "paragraph" for block in doc.content)
            or doc.deprecated
            or doc.hidden
            or doc.availability != "server and client"
            or doc.fields
            or doc.operations
            or doc.parameters
            or len(doc.returns) > 1
        )

    def _constant_type(
        self,
        environment: Environment,
        current_path: Path,
        entry: Entry,
    ) -> str:
        if entry.doc is None or not entry.doc.returns:
            return "&mdash;"
        return "<br>".join(
            self._inline(environment, current_path, type_name)
            for value in entry.doc.returns
            for type_name in self.symbol_catalog.split_inline(value.type)
        )

    def _constant_summary(
        self,
        environment: Environment,
        current_path: Path,
        entry: Entry,
    ) -> str:
        if entry.doc is None:
            return "&mdash;"

        return_descriptions = [
            self._inline(environment, current_path, value.description)
            for value in entry.doc.returns
            if value.description
        ]
        if self._constant_has_details(entry) and return_descriptions:
            return "<br>".join(return_descriptions)

        paragraphs = [
            self._inline(environment, current_path, block["content"])
            for block in entry.doc.content
            if block["type"] == "paragraph"
        ]
        if paragraphs:
            return paragraphs[0]
        return (
            "<br>".join(return_descriptions)
            or "Not documented in the source."
        )

    def _constants(
        self,
        environment: Environment,
        current_path: Path,
        page: Page,
    ) -> list[str]:
        if not page.constants:
            return []

        detailed = [
            entry for entry in page.constants if self._constant_has_details(entry)
        ]
        detailed_ids = {id(entry) for entry in detailed}
        rows = []
        for entry in page.constants:
            anchor = self.symbol_catalog.slug(entry.name)
            if id(entry) in detailed_ids:
                name = f"[`{entry.name}`](#{anchor})"
            else:
                name = f'<a id="{anchor}"></a>`{entry.name}`'
            rows.append(
                [
                    name,
                    self._constant_type(environment, current_path, entry),
                    self._constant_summary(environment, current_path, entry),
                ]
            )

        output = [
            "## Constants",
            "",
            *self._plain_table(["Name", "Type", "Description"], rows),
        ]
        for entry in detailed:
            anchor = self.symbol_catalog.slug(entry.name)
            output.extend([f"### {entry.name} {{#{anchor}}}", ""])
            value_type = self._constant_type(environment, current_path, entry)
            if value_type != "&mdash;":
                output.extend([f"**Value type:** {value_type}", ""])
            if entry.doc:
                output.extend(
                    self._doc(
                        environment,
                        current_path,
                        entry.doc,
                        4,
                        show_returns=False,
                        tables_as_lua=True,
                    )
                )
            if self._constant_values_missing(entry):
                output.extend(
                    [
                        "> **Note:**",
                        "> Values are not included in the source documentation.",
                        "",
                    ]
                )
        return output

    @staticmethod
    def _template_class_name(page: Page) -> str:
        return page.name.removesuffix("Class") or page.name

    def _template_constant_value(self, page: Page, entry: Entry) -> str:
        special_values = {
            ("ShapeClass", "colorHighlight"): 'sm.color.new("#ffffff")',
            ("ShapeClass", "colorNormal"): 'sm.color.new("#808080")',
            ("ShapeClass", "connectionInput"): (
                "sm.interactable.connectionType.none"
            ),
            ("ShapeClass", "connectionOutput"): (
                "sm.interactable.connectionType.none"
            ),
            ("ToolClass", "equipWhileSeated"): "false",
        }
        special = special_values.get((page.name, entry.name))
        if special is not None:
            return special

        doc = entry.doc
        type_name = ""
        if doc and doc.returns:
            type_name = self.symbol_catalog.inline_text(
                doc.returns[0].type
            ).casefold()

        text = ""
        if doc:
            text = " ".join(
                self.symbol_catalog.inline_text(block["content"])
                for block in doc.content
                if block["type"] == "paragraph"
            )
        match = re.search(
            r'\(\s*Defaults?(?:\s+to)?\s+(?:"([^"]*)"|([#$A-Za-z0-9_.-]+))',
            text,
            flags=re.IGNORECASE,
        )
        if match:
            quoted, value = match.groups()
            if quoted is not None:
                return json.dumps(quoted)
            value = value or ""
            lowered = value.casefold()
            if lowered in {"true", "false"}:
                return lowered
            if re.fullmatch(r"-?(?:\d+(?:\.\d*)?|\.\d+)", value):
                return value
            if lowered == "empty":
                return '""'
            if type_name == "string":
                return json.dumps(value)

        if "boolean" in type_name:
            return "false"
        if "integer" in type_name or "number" in type_name:
            return "0"
        if "string" in type_name:
            return '""'
        if "color" in type_name:
            return 'sm.color.new("#ffffff")'
        return "nil"

    def _template_return_values(self, entry: Entry) -> list[str]:
        if entry.doc is None:
            return []

        values = []
        for return_value in entry.doc.returns:
            description = self.symbol_catalog.inline_text(
                return_value.description
            ).casefold()
            type_names = self.symbol_catalog.split_inline(return_value.type)
            for type_name in type_names:
                type_name = self.symbol_catalog.inline_text(type_name).casefold()
                if type_name == "boolean":
                    value = "true" if "defaults to true" in description else "false"
                elif type_name in {"integer", "number"}:
                    value = "0"
                elif type_name == "string":
                    value = '""'
                elif type_name == "table":
                    value = "{}"
                else:
                    value = "nil"
                values.append(value)
        return values

    def _template_function(self, page: Page, entry: Entry) -> list[str]:
        parameters = [] if entry.doc is None else entry.doc.parameters
        names = [parameter.name for parameter in parameters]
        if not names or names[0] != "self":
            names.insert(0, "self")

        class_name = self._template_class_name(page)
        prefix = f"function {class_name}.{entry.name}"
        signature = f"{prefix}( {', '.join(names)} )"
        if len(signature) <= SIGNATURE_LINE_LENGTH:
            output = [signature]
        else:
            output = [f"{prefix}("]
            output.extend(
                f"    {name}{',' if index < len(names) - 1 else ''}"
                for index, name in enumerate(names)
            )
            output.append(")")

        return_values = self._template_return_values(entry)
        if return_values:
            output.append(f"    return {', '.join(return_values)}")
        output.append("end")
        return output

    def _write_class_template(self, page: Page) -> None:
        path = self._class_template_path(page)
        class_path = self.page_paths[id(page)]
        class_link = os.path.relpath(class_path, path.parent)
        class_name = self._template_class_name(page)
        code = [f"{class_name} = class()"]

        if page.constants:
            code.extend(["", "-- Constants"])
            for entry in page.constants:
                code.extend(
                    [
                        f"-- Docs: {page.name}.html#"
                        f"{self.symbol_catalog.slug(entry.name)}",
                        f"{class_name}.{entry.name} = "
                        f"{self._template_constant_value(page, entry)}",
                    ]
                )

        callbacks = page.common_callbacks + page.callbacks
        sides = (
            ("server_", "Server callbacks"),
            ("client_", "Client callbacks"),
        )
        for side, title in sides:
            entries = [entry for entry in callbacks if entry.name.startswith(side)]
            if not entries:
                continue
            code.extend(["", f"-- {title}"])
            for entry in entries:
                code.extend(
                    [
                        f"-- Docs: {page.name}.html#"
                        f"{self.symbol_catalog.slug(entry.name)}",
                        *self._template_function(page, entry),
                        "",
                    ]
                )
            if code[-1] == "":
                code.pop()

        output = [
            f"# {page.name} script template",
            "",
            f"[Back to {page.name}]({Path(class_link).as_posix()})",
            "",
            "Copy this starter script and remove anything you do not need.",
            "",
            "```lua",
            *code,
            "```",
            "",
        ]
        path.write_text("\n".join(output), encoding="utf-8")

    def _member_access(
        self,
        environment: Environment,
        current_path: Path,
        label: str,
        doc: Doc,
    ) -> list[str]:
        availability = ""
        if doc.availability != "server and client":
            availability = f" ({doc.availability.title()}-Only)"
        if doc.hidden:
            availability += " (Hidden)"

        content = self._blocks(environment, current_path, doc.content)
        while content and content[-1] == "":
            content.pop()

        output = [f"    - `{label}`:{availability}"]
        if content and not content[0].startswith(("```", "- ", "| ", ">")):
            output[0] += f" {content.pop(0)}"
            if content and content[0] == "":
                content.pop(0)

        if content:
            output.append("")
            output.extend(f"        {line}" if line else "" for line in content)

        if doc.deprecated:
            deprecated = self._blocks(environment, current_path, doc.deprecated)
            while deprecated and deprecated[-1] == "":
                deprecated.pop()
            output.append("")
            output.append("        **Deprecated:**")
            output.extend(f"        {line}" if line else "" for line in deprecated)

        return output

    def _members(
        self,
        environment: Environment,
        current_path: Path,
        page: Page,
    ) -> list[str]:
        if not page.members:
            return []

        output = ["**Values:**", ""]
        for member in page.members:
            type_name = self._inline(
                environment,
                current_path,
                self.symbol_catalog.member_type(page, member),
            )
            output.append(
                f'- <a id="{self.symbol_catalog.slug(member.name)}"></a>'
                f'`{member.name}` [ **{type_name}** ] <br>'
            )
            if member.get:
                output.extend(
                    self._member_access(
                        environment, current_path, "Get", member.get
                    )
                )
            if member.set:
                output.extend(
                    self._member_access(
                        environment, current_path, "Set", member.set
                    )
                )
            output.append("")
        return output

    def _write_page(self, environment: Environment, kind: str, page: Page) -> None:
        path = self.page_paths[id(page)]
        path.parent.mkdir(parents=True, exist_ok=True)
        output = [f"# {self._page_display_name(page)}", ""]

        if kind == "class":
            template_path = self._class_template_path(page)
            template_link = os.path.relpath(template_path, path.parent)
            output.extend(
                [
                    "**Script template:** "
                    f"[View starter script]({Path(template_link).as_posix()})",
                    "",
                ]
            )

        if page.associated_type:
            link = self._link(
                environment, path, page.associated_type, page.associated_type
            )
            output.extend([f"**Associated type:** {link}", ""])
        if page.associated_namespace:
            link = self._link(
                environment,
                path,
                page.associated_namespace,
                page.associated_namespace,
            )
            output.extend([f"**Associated namespace:** {link}", ""])
        if page.usage:
            output.extend([f"**Usage:** {page.usage.capitalize()}", ""])
        if page.serializable is not None:
            output.extend(
                [f"**Serializable:** {'Yes' if page.serializable else 'No'}", ""]
            )
        if page.doc:
            output.extend(self._doc(environment, path, page.doc, 2))

        output.extend(self._constants(environment, path, page))

        output.extend(self._members(environment, path, page))

        output.extend(self._operations(environment, path, page.metamethods))
        output.extend(self._methods(environment, path, kind, page))
        if kind == "class":
            output.extend(self._callbacks(environment, path, page))

        path.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")

    def _write_markdown_index(self) -> None:
        introduction = INTRODUCTION_PATH.read_text(encoding="utf-8").rstrip()
        (self.markdown_root / "index.md").write_text(
            introduction + "\n", encoding="utf-8"
        )

    def _write_search_page(self) -> None:
        (self.markdown_root / "search.md").write_text(
            SEARCH_PATH.read_text(encoding="utf-8"),
            encoding="utf-8",
        )

    def _write_environment_index(self, environment: Environment) -> None:
        directory = self.markdown_root / self._environment_directory(environment)
        directory.mkdir(parents=True, exist_ok=True)
        output = [f"# {environment.name} script environment", ""]
        for kind, pages in self._navigation_groups(environment):
            if pages:
                category = CATEGORY_DIRECTORIES[kind]
                output.append(f"- [{CATEGORY_TITLES[kind]}]({category}/index.md)")
        output.append("")
        (directory / "index.md").write_text("\n".join(output), encoding="utf-8")

    def _write_category_index(
        self, environment: Environment, kind: str, pages: list[Page]
    ) -> None:
        if not pages:
            return
        directory = (
            self.markdown_root
            / self._environment_directory(environment)
            / CATEGORY_DIRECTORIES[kind]
        )
        directory.mkdir(parents=True, exist_ok=True)
        output = [f"# {CATEGORY_TITLES[kind]}", ""]
        for page in sorted(pages, key=self._page_sort_key):
            path = self.page_paths[id(page)]
            display_name = self._page_display_name(page)
            output.append(f"- [`{display_name}`]({path.name})")
        output.append("")
        (directory / "index.md").write_text("\n".join(output), encoding="utf-8")
