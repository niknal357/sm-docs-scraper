from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha1
from html import escape, unescape
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
from typing import Iterable
from urllib.parse import unquote, urlsplit

import markdown
from pygments.formatters import HtmlFormatter

from make_ir import Doc, Documentation, Entry, Environment, Inline, Page


_ENVIRONMENT_DIRECTORIES = {
    "Game": "Game-Script-Environment",
    "Terrain": "Terrain-Script-Environment",
}
_CATEGORY_DIRECTORIES = {
    "namespace": "Static-Functions",
    "userdata": "Userdata",
    "class": "Classes",
}
_CATEGORY_TITLES = {
    "namespace": "Static Functions",
    "userdata": "Userdata",
    "class": "Classes",
}
_TOC_EXCLUDED_SECTIONS = {"constants", "fields", "members", "operations"}
_SIGNATURE_LINE_LENGTH = 80
_SIGNATURE_FENCE = "``` { .lua .api-signature }"
_INTRODUCTION_PATH = Path(__file__).parent / "content" / "introduction.md"
_BINARY_OPERATORS = {
    "__add": "+",
    "__div": "/",
    "__eq": "==",
    "__lt": "<",
    "__mul": "*",
    "__sub": "-",
}
_LEGACY_EMPTY_LINK = re.compile(
    r'<a href="index\.html#(?:server|client|console)">(.*?)</a>',
    flags=re.IGNORECASE,
)


@dataclass
class CallbackGroup:
    name: str
    server: Entry | None = None
    client: Entry | None = None


@dataclass(frozen=True)
class MethodAnchor:
    anchor: str
    label: str
    legacy_alias: str | None = None


class _HtmlLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.toc_depth = 0
        self.toc_hrefs: list[str] = []
        self.toc_labels: list[str] = []
        self._toc_label: list[str] | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id is not None:
            self.ids.append(element_id)

        if tag == "aside" and "table-of-contents" in (
            attributes.get("class") or ""
        ).split():
            self.toc_depth += 1

        href = attributes.get("href") if tag == "a" else None
        if href is not None:
            self.hrefs.append(href)
            if self.toc_depth:
                self.toc_hrefs.append(href)
                self._toc_label = []

    def handle_data(self, data: str) -> None:
        if self._toc_label is not None:
            self._toc_label.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "a" and self._toc_label is not None:
            self.toc_labels.append("".join(self._toc_label).strip())
            self._toc_label = None
        if tag == "aside" and self.toc_depth:
            self.toc_depth -= 1


class DocumentationRenderer:
    def __init__(self, docs: Documentation, markdown_root: Path, html_root: Path):
        self.docs = docs
        self.markdown_root = markdown_root
        self.html_root = html_root
        self.page_paths: dict[int, Path] = {}
        self.references: dict[str, dict[str, tuple[Path, str | None]]] = {}
        self._index_references()

    def _index_references(self) -> None:
        for environment in self.docs.environments:
            references: dict[str, tuple[Path, str | None]] = {}
            self.references[environment.name] = references

            for kind, pages in self._page_groups(environment):
                for page in pages:
                    path = self._page_path(environment, kind, page)
                    self.page_paths[id(page)] = path
                    references[page.name] = (path, None)

                    entries = (
                        page.constants
                        + page.functions
                        + page.members
                        + page.metamethods
                        + page.common_callbacks
                        + page.callbacks
                    )
                    for entry in entries:
                        references.setdefault(
                            f"{page.name}.{entry.name}",
                            (path, self._slug(entry.name)),
                        )

                    if kind == "class":
                        for callback in self._callback_groups(page):
                            references[f"{page.name}.{callback.name}"] = (
                                path,
                                self._slug(callback.name),
                            )

                    if page.name == "GLOBAL":
                        for entry in page.constants + page.functions:
                            references.setdefault(
                                entry.name, (path, self._slug(entry.name))
                            )

    def render(self) -> tuple[Path, Path]:
        shutil.rmtree(self.markdown_root, ignore_errors=True)
        shutil.rmtree(self.html_root, ignore_errors=True)
        self.markdown_root.mkdir(parents=True)

        self._write_markdown_index()
        for environment in self.docs.environments:
            self._write_environment_index(environment)
            for kind, pages in self._page_groups(environment):
                self._write_category_index(environment, kind, pages)
                for page in pages:
                    self._write_page(environment, kind, page)
                    if kind == "class":
                        self._write_class_template(page)

        self._write_html_tree()
        self._validate_html_tree()
        return self.markdown_root, self.html_root

    @staticmethod
    def _page_groups(environment: Environment) -> Iterable[tuple[str, list[Page]]]:
        return (
            ("namespace", environment.namespaces),
            ("userdata", environment.userdata),
            ("class", environment.classes),
        )

    def _navigation_groups(
        self, environment: Environment
    ) -> list[tuple[str, list[Page]]]:
        return sorted(
            self._page_groups(environment),
            key=lambda group: _CATEGORY_TITLES[group[0]].casefold(),
        )

    def _environment_directory(self, environment: Environment) -> str:
        return _ENVIRONMENT_DIRECTORIES.get(
            environment.name, f"{environment.name}-Script-Environment"
        )

    def _page_path(self, environment: Environment, kind: str, page: Page) -> Path:
        filename = "Global" if page.name == "GLOBAL" else page.name
        return (
            self.markdown_root
            / self._environment_directory(environment)
            / _CATEGORY_DIRECTORIES[kind]
            / f"{filename}.md"
        )

    def _class_template_path(self, page: Page) -> Path:
        return self.page_paths[id(page)].with_name(f"{page.name}-Template.md")

    @staticmethod
    def _slug(name: str) -> str:
        return re.sub(r"[^a-z0-9_-]+", "-", name.lower()).strip("-")

    @staticmethod
    def _page_sort_key(page: Page) -> str:
        return page.name.casefold()

    @staticmethod
    def _page_display_name(page: Page) -> str:
        return "Global" if page.name == "GLOBAL" else page.name

    @staticmethod
    def _instance_name(type_name: str) -> str:
        return type_name[:1].lower() + type_name[1:]

    def _link(
        self,
        environment: Environment,
        current_path: Path,
        target: str,
        label: str,
    ) -> str:
        destination = self.references[environment.name].get(target)
        if destination is None:
            return f"`{label}`"

        destination_path, anchor = destination
        if destination_path == current_path and anchor:
            href = f"#{anchor}"
        else:
            href = os.path.relpath(destination_path, current_path.parent)
            href = Path(href).as_posix()
            if anchor:
                href += f"#{anchor}"
        return f"[{label}]({href})"

    def _inline(
        self, environment: Environment, current_path: Path, content: Inline
    ) -> str:
        rendered = []
        for part in content:
            if isinstance(part, str):
                rendered.append(_LEGACY_EMPTY_LINK.sub(r"\1", part))
                continue
            target = part["reference"]
            label = part.get("label", target)
            rendered.append(self._link(environment, current_path, target, label))
        return "".join(rendered)

    @staticmethod
    def _inline_text(content: Inline) -> str:
        return "".join(
            part
            if isinstance(part, str)
            else part.get("label", part["reference"])
            for part in content
        )

    @staticmethod
    def _split_inline(content: Inline, delimiter: str = ",") -> list[Inline]:
        parts: list[Inline] = [[]]
        for item in content:
            if not isinstance(item, str):
                parts[-1].append(item)
                continue

            chunks = item.split(delimiter)
            parts[-1].append(chunks[0])
            for chunk in chunks[1:]:
                parts.append([chunk])

        for part in parts:
            if part and isinstance(part[0], str):
                part[0] = part[0].lstrip()
            if part and isinstance(part[-1], str):
                part[-1] = part[-1].rstrip()
            part[:] = [item for item in part if item != ""]
        return parts

    def _blocks(
        self,
        environment: Environment,
        current_path: Path,
        blocks: list[dict],
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

    def _doc(
        self,
        environment: Environment,
        current_path: Path,
        doc: Doc,
        detail_heading: int,
        show_availability: bool = True,
    ) -> list[str]:
        output: list[str] = []

        if doc.hidden:
            output.extend(["**Visibility:** Hidden", ""])
        if show_availability and doc.availability != "server and client":
            output.extend([f"**Availability:** {doc.availability.title()} only", ""])
        if doc.deprecated:
            output.extend(["> **Deprecated:**", *self._quote_blocks(environment, current_path, doc.deprecated), ""])

        output.extend(self._blocks(environment, current_path, doc.content))
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

        if doc.returns:
            output.extend(["**Returns:**", ""])
            rows = [
                [
                    self._inline(environment, current_path, item.type),
                    self._inline(environment, current_path, item.description),
                ]
                for item in doc.returns
            ]
            output.extend(self._plain_table(["Type", "Description"], rows))

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
            cells = [cell.replace("|", "\\|") for cell in row]
            output.append("| " + " | ".join(cells) + " |")
        output.append("")
        return output

    def _operation_signature(
        self, name: str, signature: Inline
    ) -> tuple[str, Inline]:
        parts = self._split_inline(signature)
        if name in _BINARY_OPERATORS and len(parts) == 3:
            left = self._inline_text(parts[0])
            right = self._inline_text(parts[1])
            return f"{left} {_BINARY_OPERATORS[name]} {right}", parts[2]
        if name == "__unm" and len(parts) == 2:
            return f"-{self._inline_text(parts[0])}", parts[1]
        if name == "__tostring" and len(parts) == 2:
            return f"tostring({self._inline_text(parts[0])})", parts[1]
        raise ValueError(f"Unsupported operation signature: {name}")

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
                expression, result = self._operation_signature(
                    entry.name, operation.signature
                )
                anchor = (
                    f'<a id="{self._slug(entry.name)}"></a>' if index == 0 else ""
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

    def _entry_parameters(self, kind: str, page: Page, entry: Entry) -> list:
        if entry.doc is None:
            return []

        parameters = entry.doc.parameters
        if kind == "class" and parameters and parameters[0].name == "self":
            return parameters[1:]
        if kind == "userdata" and parameters:
            first_type = parameters[0].type
            if first_type == [{"reference": page.name}]:
                return parameters[1:]
        return parameters

    def _method_anchors(
        self, kind: str, page: Page, entries: list[Entry]
    ) -> dict[int, MethodAnchor]:
        name_counts = Counter(self._slug(entry.name) for entry in entries)
        used: set[str] = set()
        first_overload: set[str] = set()
        anchors: dict[int, MethodAnchor] = {}

        for entry in entries:
            base = self._slug(entry.name)
            if name_counts[base] == 1:
                anchors[id(entry)] = MethodAnchor(anchor=base, label=entry.name)
                used.add(base)
                continue

            parameters = self._entry_parameters(kind, page, entry)
            display_types = [
                self._inline_text(parameter.type)
                + ("?" if parameter.optional else "")
                for parameter in parameters
            ]
            label = f"{entry.name}({', '.join(display_types)})"
            suffix_parts = []
            for parameter in parameters:
                type_slug = self._slug(self._inline_text(parameter.type)) or "any"
                if parameter.optional:
                    type_slug += "-optional"
                suffix_parts.append(type_slug)
            suffix = "-".join(suffix_parts) or "no-arguments"
            candidate = f"{base}-{suffix}"

            if candidate in used:
                detailed_signature = ",".join(
                    f"{parameter.name}:{self._inline_text(parameter.type)}:"
                    f"{'optional' if parameter.optional else 'required'}"
                    for parameter in parameters
                )
                digest = sha1(detailed_signature.encode("utf-8")).hexdigest()[:8]
                candidate = f"{candidate}-{digest}"
            ordinal = 2
            unique_candidate = candidate
            while unique_candidate in used:
                unique_candidate = f"{candidate}-{ordinal}"
                ordinal += 1

            legacy_alias = None
            if base not in first_overload:
                legacy_alias = base
                first_overload.add(base)
                used.add(base)
            used.add(unique_candidate)
            anchors[id(entry)] = MethodAnchor(
                anchor=unique_candidate,
                label=label,
                legacy_alias=legacy_alias,
            )

        return anchors

    def _signature(self, kind: str, page: Page, entry: Entry) -> str:
        if entry.doc is None:
            return entry.name

        parameters = self._entry_parameters(kind, page, entry)
        names = [
            f"{parameter.name}?" if parameter.optional else parameter.name
            for parameter in parameters
        ]
        arguments = ", ".join(names)

        if kind == "namespace":
            prefix = "" if page.name == "GLOBAL" else f"{page.name}."
        elif kind == "userdata":
            prefix = f"{self._instance_name(page.name)}:"
        else:
            prefix = f"{page.name}:"

        signature = f"{prefix}{entry.name}( {arguments} )"
        if len(signature) <= _SIGNATURE_LINE_LENGTH or not names:
            return signature

        lines = [f"{prefix}{entry.name}("]
        lines.extend(
            f"    {name}{',' if index < len(names) - 1 else ''}"
            for index, name in enumerate(names)
        )
        lines.append(")")
        return "\n".join(lines)

    @staticmethod
    def _callback_groups(page: Page) -> list[CallbackGroup]:
        groups: dict[str, CallbackGroup] = {}
        for entry in page.common_callbacks + page.callbacks:
            if entry.name.startswith("server_"):
                side = "server"
                name = entry.name.removeprefix("server_")
            elif entry.name.startswith("client_"):
                side = "client"
                name = entry.name.removeprefix("client_")
            else:
                raise ValueError(f"Unknown callback side: {entry.name}")

            group = groups.setdefault(name, CallbackGroup(name=name))
            if getattr(group, side) is not None:
                raise ValueError(f"Duplicate {side} callback: {page.name}.{name}")
            setattr(group, side, entry)
        return list(groups.values())

    def _callback_aliases(self, callback: CallbackGroup) -> list[str]:
        return [
            f'<a id="{self._slug(entry.name)}"></a>'
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
        anchor = self._slug(callback.name)
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
                    _SIGNATURE_FENCE,
                    self._signature("class", page, server),
                    self._signature("class", page, client),
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
                    _SIGNATURE_FENCE,
                    self._signature("class", page, entry),
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
        groups = self._callback_groups(page)
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
        method_anchors = self._method_anchors(kind, page, page.functions)
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
                        _SIGNATURE_FENCE,
                        self._signature(kind, page, entry),
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

    def _entries(
        self,
        environment: Environment,
        current_path: Path,
        kind: str,
        page: Page,
        title: str,
        entries: list[Entry],
    ) -> list[str]:
        if not entries:
            return []

        output = [f"## {title}", ""]
        for entry in entries:
            anchor = self._slug(entry.name)
            output.extend([f"### {entry.name} {{#{anchor}}}", ""])
            if title != "Constants":
                output.extend(
                    [
                        _SIGNATURE_FENCE,
                        self._signature(kind, page, entry),
                        "```",
                        "",
                    ]
                )
            if entry.doc:
                output.extend(self._doc(environment, current_path, entry.doc, 4))
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
            type_name = self._inline_text(doc.returns[0].type).casefold()

        text = ""
        if doc:
            text = " ".join(
                self._inline_text(block["content"])
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
            description = self._inline_text(return_value.description).casefold()
            type_names = self._inline_text(return_value.type).split(",")
            for type_name in type_names:
                type_name = type_name.strip().casefold()
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
        if len(signature) <= _SIGNATURE_LINE_LENGTH:
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
                        f"-- Docs: {page.name}.html#{self._slug(entry.name)}",
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
                        f"-- Docs: {page.name}.html#{self._slug(entry.name)}",
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

    @staticmethod
    def _member_type(page: Page, member: Entry) -> Inline:
        if member.get and member.get.returns:
            return member.get.returns[0].type

        if member.set and member.set.parameters:
            parameters = member.set.parameters
            if parameters[0].type == [{"reference": page.name}]:
                parameters = parameters[1:]
            if parameters:
                return parameters[-1].type

        return ["unknown"]

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
                environment, current_path, self._member_type(page, member)
            )
            output.append(
                f'- <a id="{self._slug(member.name)}"></a>`{member.name}` '
                f"[ **{type_name}** ] <br>"
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
            output.extend([f"**Usage:** {page.usage.title()}", ""])
        if page.serializable is not None:
            output.extend(
                [f"**Serializable:** {'Yes' if page.serializable else 'No'}", ""]
            )
        if page.doc:
            output.extend(self._doc(environment, path, page.doc, 2))

        output.extend(
            self._entries(
                environment, path, kind, page, "Constants", page.constants
            )
        )

        output.extend(self._members(environment, path, page))

        output.extend(self._operations(environment, path, page.metamethods))
        output.extend(self._methods(environment, path, kind, page))
        if kind == "class":
            output.extend(self._callbacks(environment, path, page))

        path.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")

    def _write_markdown_index(self) -> None:
        introduction = _INTRODUCTION_PATH.read_text(encoding="utf-8").rstrip()
        (self.markdown_root / "index.md").write_text(
            introduction + "\n", encoding="utf-8"
        )

    def _write_environment_index(self, environment: Environment) -> None:
        directory = self.markdown_root / self._environment_directory(environment)
        directory.mkdir(parents=True, exist_ok=True)
        output = [f"# {environment.name} script environment", ""]
        for kind, pages in self._navigation_groups(environment):
            if pages:
                category = _CATEGORY_DIRECTORIES[kind]
                output.append(f"- [{_CATEGORY_TITLES[kind]}]({category}/index.md)")
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
            / _CATEGORY_DIRECTORIES[kind]
        )
        directory.mkdir(parents=True, exist_ok=True)
        output = [f"# {_CATEGORY_TITLES[kind]}", ""]
        for page in sorted(pages, key=self._page_sort_key):
            path = self.page_paths[id(page)]
            display_name = self._page_display_name(page)
            output.append(f"- [`{display_name}`]({path.name})")
        output.append("")
        (directory / "index.md").write_text("\n".join(output), encoding="utf-8")

    def _html_href(self, current_html: Path, target_markdown: Path) -> str:
        target_html = self.html_root / target_markdown.relative_to(
            self.markdown_root
        ).with_suffix(".html")
        return Path(os.path.relpath(target_html, current_html.parent)).as_posix()

    def _sidebar(self, current_markdown: Path, current_html: Path) -> str:
        output = []
        root_index = self.markdown_root / "index.md"
        root_class = " active" if current_markdown == root_index else ""
        output.append(
            f'<a class="sidebar-overview{root_class}" '
            f'href="{self._html_href(current_html, root_index)}">Introduction</a>'
        )

        for environment in sorted(
            self.docs.environments, key=lambda item: item.name.casefold()
        ):
            environment_directory = (
                self.markdown_root / self._environment_directory(environment)
            )
            environment_active = current_markdown.is_relative_to(
                environment_directory
            )
            open_attribute = " open" if environment_active else ""
            output.append(
                f'<details class="sidebar-group" '
                f'data-sidebar-key="environment:{escape(environment.name)}"{open_attribute}>'
            )
            output.append(
                f"<summary>{escape(environment.name)} Script Environment</summary>"
            )
            output.append('<div class="sidebar-group-content">')

            for kind, pages in self._navigation_groups(environment):
                if not pages:
                    continue
                category_directory = environment_directory / _CATEGORY_DIRECTORIES[kind]
                category_active = current_markdown.is_relative_to(category_directory)
                category_open = " open" if category_active else ""
                output.append(
                    f'<details class="sidebar-category" '
                    f'data-sidebar-key="environment:{escape(environment.name)}:'
                    f'category:{kind}"{category_open}>'
                )
                output.append(
                    f"<summary>{escape(_CATEGORY_TITLES[kind])}</summary>"
                )
                output.append("<ul>")
                for page in sorted(pages, key=self._page_sort_key):
                    page_path = self.page_paths[id(page)]
                    active_class = " active" if current_markdown == page_path else ""
                    display_name = self._page_display_name(page)
                    output.append(
                        f'<li class="sidebar-page"><a class="{active_class.strip()}" '
                        f'href="{self._html_href(current_html, page_path)}">'
                        f"{escape(display_name)}</a></li>"
                    )
                output.extend(["</ul>", "</details>"])

            output.extend(["</div>", "</details>"])
        return "\n".join(output)

    def _breadcrumbs(self, current_markdown: Path, current_html: Path) -> str:
        relative = current_markdown.relative_to(self.markdown_root)
        output = [
            f'<a href="{self._html_href(current_html, self.markdown_root / "index.md")}">Docs</a>'
        ]
        labels = {
            "Game-Script-Environment": "Game",
            "Terrain-Script-Environment": "Terrain",
            "Static-Functions": "Static Functions",
        }

        directories = relative.parts[:-1]
        for index, part in enumerate(directories):
            target = self.markdown_root.joinpath(*directories[: index + 1], "index.md")
            output.append('<span class="breadcrumb-separator">›</span>')
            output.append(
                f'<a href="{self._html_href(current_html, target)}">'
                f"{escape(labels.get(part, part))}</a>"
            )

        if relative.name != "index.md":
            output.append('<span class="breadcrumb-separator">›</span>')
            output.append(f"<span>{escape(relative.stem)}</span>")
        return "".join(output)

    @staticmethod
    def _table_of_contents(body: str) -> str:
        items = []
        include_children = True
        for level, anchor, label in re.findall(
            r'<h([23]) id="([^"]+)">(.*?)</h\1>', body, flags=re.DOTALL
        ):
            if level == "2":
                include_children = anchor not in _TOC_EXCLUDED_SECTIONS
            if not include_children:
                continue

            text = unescape(re.sub(r"<[^>]+>", "", label))
            items.append(
                f'<li class="toc-level-{level}"><a href="#{escape(anchor)}">'
                f"{escape(text)}</a></li>"
            )
        if not items:
            return ""
        return "<ul>" + "".join(items) + "</ul>"

    @staticmethod
    def _render_optional_signature_markers(body: str) -> str:
        optional_marker = (
            '<span class="p optional-marker" aria-hidden="true"></span>'
        )

        def replace_marker(match: re.Match[str]) -> str:
            signature = match.group(0)
            return signature.replace(
                '<span class="err">?</span>', optional_marker
            )

        return re.sub(
            r'<div class="[^"]*\bapi-signature\b[^"]*">.*?</div>',
            replace_marker,
            body,
            flags=re.DOTALL,
        )

    def _write_html_tree(self) -> None:
        self.html_root.mkdir(parents=True)
        assets = self.html_root / "assets"
        assets.mkdir()
        light_highlight_style = HtmlFormatter(style="default").get_style_defs(
            ".codehilite"
        )
        dark_highlight_style = HtmlFormatter(style="one-dark").get_style_defs(
            ':root[data-theme="dark"] .codehilite'
        )
        (assets / "style.css").write_text(
            f"{_STYLE}\n{light_highlight_style}\n{dark_highlight_style}\n",
            encoding="utf-8",
        )

        for markdown_path in self.markdown_root.rglob("*.md"):
            relative = markdown_path.relative_to(self.markdown_root)
            html_path = self.html_root / relative.with_suffix(".html")
            html_path.parent.mkdir(parents=True, exist_ok=True)
            body = markdown.markdown(
                markdown_path.read_text(encoding="utf-8"),
                extensions=[
                    "codehilite",
                    "fenced_code",
                    "sane_lists",
                    "tables",
                    "toc",
                    "attr_list",
                ],
                extension_configs={
                    "codehilite": {
                        "guess_lang": False,
                        "noclasses": False,
                        "use_pygments": True,
                    }
                },
            )
            body = self._render_optional_signature_markers(body)
            body = re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', body)
            stylesheet = os.path.relpath(assets / "style.css", html_path.parent)
            home = os.path.relpath(self.html_root / "index.html", html_path.parent)
            title = relative.stem if relative.stem != "index" else relative.parent.name
            html_path.write_text(
                _HTML_TEMPLATE.format(
                    title=escape(title or "Scrap Mechanic API"),
                    stylesheet=Path(stylesheet).as_posix(),
                    home=Path(home).as_posix(),
                    sidebar=self._sidebar(markdown_path, html_path),
                    breadcrumbs=self._breadcrumbs(markdown_path, html_path),
                    body=body,
                    toc=self._table_of_contents(body),
                    theme_script=_THEME_SCRIPT,
                    script=_SCRIPT,
                ),
                encoding="utf-8",
            )

    def _validate_html_tree(self) -> None:
        html_root = self.html_root.resolve()
        parsed: dict[Path, _HtmlLinks] = {}
        errors: list[str] = []

        for path in sorted(html_root.rglob("*.html")):
            parser = _HtmlLinks()
            parser.feed(path.read_text(encoding="utf-8"))
            parsed[path] = parser

            relative = path.relative_to(html_root)
            duplicate_ids = sorted(
                element_id
                for element_id, count in Counter(parser.ids).items()
                if count > 1
            )
            if duplicate_ids:
                errors.append(
                    f"{relative}: duplicate IDs: {', '.join(duplicate_ids)}"
                )

            duplicate_toc_targets = sorted(
                href
                for href, count in Counter(parser.toc_hrefs).items()
                if count > 1
            )
            if duplicate_toc_targets:
                errors.append(
                    f"{relative}: duplicate TOC targets: "
                    f"{', '.join(duplicate_toc_targets)}"
                )

            duplicate_toc_labels = sorted(
                label
                for label, count in Counter(parser.toc_labels).items()
                if count > 1
            )
            if duplicate_toc_labels:
                errors.append(
                    f"{relative}: duplicate TOC labels: "
                    f"{', '.join(duplicate_toc_labels)}"
                )

        for source, parser in parsed.items():
            for href in parser.hrefs:
                destination = urlsplit(href)
                if destination.scheme or destination.netloc:
                    continue

                if not destination.path:
                    target = source
                elif destination.path.startswith("/"):
                    target = html_root / unquote(destination.path).lstrip("/")
                else:
                    target = source.parent / unquote(destination.path)
                target = target.resolve()
                source_relative = source.relative_to(html_root)

                if not target.is_relative_to(html_root):
                    errors.append(f"{source_relative}: link escapes site: {href}")
                    continue
                if not target.is_file():
                    errors.append(f"{source_relative}: missing link target: {href}")
                    continue
                if destination.fragment:
                    target_parser = parsed.get(target)
                    fragment = unquote(destination.fragment)
                    if target_parser is None or fragment not in target_parser.ids:
                        errors.append(
                            f"{source_relative}: missing fragment: {href}"
                        )

        if errors:
            displayed = errors[:50]
            if len(errors) > len(displayed):
                displayed.append(f"... and {len(errors) - len(displayed)} more")
            raise ValueError(
                "Generated HTML validation failed:\n- " + "\n- ".join(displayed)
            )


def render_docs(
    docs: Documentation,
    markdown_root: Path | str,
    html_root: Path | str,
) -> tuple[Path, Path]:
    renderer = DocumentationRenderer(
        docs, Path(markdown_root), Path(html_root)
    )
    return renderer.render()


_HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | SM Docs</title>
  <script>{theme_script}</script>
  <link rel="stylesheet" href="{stylesheet}">
</head>
<body>
  <header class="navbar">
    <button class="menu-button" id="menu-button" aria-label="Toggle navigation">☰</button>
    <a class="brand" href="{home}"><span class="brand-mark">SM</span><span>SM Docs</span></a>
    <div class="navbar-spacer"></div>
    <button class="theme-button" id="theme-button" type="button" aria-label="Toggle color theme"><svg class="theme-icon theme-icon-sun" aria-hidden="true" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"></circle><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"></path></svg><svg class="theme-icon theme-icon-moon" aria-hidden="true" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79Z"></path></svg></button>
    <label class="search"><svg aria-hidden="true" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"></circle><path d="m16 16 5 5"></path></svg><input id="doc-search" type="search" placeholder="Filter pages"></label>
  </header>
  <div class="page-layout">
    <aside class="sidebar" id="sidebar"><nav>{sidebar}</nav></aside>
    <div class="content-layout">
      <main class="doc">
        <div class="breadcrumbs">{breadcrumbs}</div>
        {body}
      </main>
      <aside class="table-of-contents">{toc}</aside>
    </div>
  </div>
  <script>{script}</script>
</body>
</html>
"""

_THEME_SCRIPT = """(() => {
  let theme;
  try {
    theme = localStorage.getItem('sm-docs-theme');
  } catch (_) {}
  if (theme !== 'light' && theme !== 'dark') {
    theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }
  document.documentElement.dataset.theme = theme;
})();"""

_SCRIPT = """const themeButton = document.getElementById('theme-button');
const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
const updateThemeButton = () => {
  const dark = document.documentElement.dataset.theme === 'dark';
  const nextTheme = dark ? 'light' : 'dark';
  themeButton.setAttribute('aria-label', `Switch to ${nextTheme} mode`);
  themeButton.title = `Switch to ${nextTheme} mode`;
};
const applyTheme = (theme) => {
  document.documentElement.dataset.theme = theme;
  updateThemeButton();
};
const savedTheme = () => {
  try {
    const theme = localStorage.getItem('sm-docs-theme');
    return theme === 'light' || theme === 'dark' ? theme : null;
  } catch (_) {
    return null;
  }
};
updateThemeButton();
themeButton.addEventListener('click', () => {
  const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  applyTheme(theme);
  try {
    localStorage.setItem('sm-docs-theme', theme);
  } catch (_) {}
});
if ('addEventListener' in systemTheme) {
  systemTheme.addEventListener('change', (event) => {
    if (!savedTheme()) applyTheme(event.matches ? 'dark' : 'light');
  });
}

const menu = document.getElementById('menu-button');
const sidebar = document.getElementById('sidebar');
menu.addEventListener('click', () => document.body.classList.toggle('sidebar-open'));
const statePrefix = 'sm-docs-sidebar:';
const groups = sidebar.querySelectorAll('details[data-sidebar-key]');
groups.forEach((group) => {
  const key = statePrefix + group.dataset.sidebarKey;
  try {
    const saved = sessionStorage.getItem(key);
    if (saved !== null) {
      group.open = saved === 'open';
    } else {
      sessionStorage.setItem(key, group.open ? 'open' : 'closed');
    }
  } catch (_) {}
  group.addEventListener('toggle', () => {
    try {
      sessionStorage.setItem(key, group.open ? 'open' : 'closed');
    } catch (_) {}
  });
});
const activeLink = sidebar.querySelector('a.active');
if (activeLink) {
  let parent = activeLink.parentElement;
  while (parent) {
    if (parent.tagName === 'DETAILS') parent.open = true;
    parent = parent.parentElement;
  }
  const sidebarRect = sidebar.getBoundingClientRect();
  const activeRect = activeLink.getBoundingClientRect();
  sidebar.scrollTop += activeRect.top - sidebarRect.top - sidebarRect.height / 2;
}
const search = document.getElementById('doc-search');
search.addEventListener('input', () => {
  const query = search.value.trim().toLowerCase();
  document.querySelectorAll('.sidebar-page').forEach((item) => {
    const matches = !query || item.textContent.toLowerCase().includes(query);
    item.hidden = !matches;
    if (query && matches) {
      let parent = item.parentElement;
      while (parent) {
        if (parent.tagName === 'DETAILS') parent.open = true;
        parent = parent.parentElement;
      }
    }
  });
});
"""

_STYLE = """:root {
  color-scheme: light;
  --primary: #2e8555;
  --primary-dark: #277148;
  --brand-background: #2e8555;
  --background: #ffffff;
  --surface: #ffffff;
  --surface-muted: #f5f6f7;
  --active-background: #e7f4ec;
  --blockquote-background: #edf7f1;
  --code-background: #f8f8f8;
  --code-text: #1c1e21;
  --inline-code-background: #f1f3f5;
  --text: #1c1e21;
  --sidebar-text: #3b3b3b;
  --border: #dadde1;
  --muted: #606770;
  --shadow: rgb(0 0 0 / 8%);
  --radius: 0;
  --sidebar-width: 300px;
  --navbar-height: 60px;
}
:root[data-theme="dark"] {
  color-scheme: dark;
  --primary: #55c98d;
  --primary-dark: #72dda4;
  --brand-background: #277148;
  --background: #181a1f;
  --surface: #202329;
  --surface-muted: #2a2e35;
  --active-background: #183b2a;
  --blockquote-background: #1d3328;
  --code-background: #282c34;
  --code-text: #f8f9fa;
  --inline-code-background: #2b3038;
  --text: #e6e9ed;
  --sidebar-text: #d5dae0;
  --border: #3b414a;
  --muted: #a7afb9;
  --shadow: rgb(0 0 0 / 30%);
}
*, *::before, *::after {
  border-radius: var(--radius);
  box-sizing: border-box;
}
html { scroll-padding-top: 76px; }
body {
  background: var(--background);
  color: var(--text);
  font: 16px/1.65 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  margin: 0;
}
a { color: var(--primary); text-decoration: none; }
a:hover { text-decoration: underline; }
.navbar {
  align-items: center;
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  box-shadow: 0 1px 2px var(--shadow);
  display: flex;
  gap: 1.4rem;
  height: var(--navbar-height);
  padding: 0 1.4rem;
  position: sticky;
  top: 0;
  z-index: 20;
}
.brand {
  align-items: center;
  color: var(--text);
  display: flex;
  font-size: 1.15rem;
  font-weight: 700;
  gap: 0.6rem;
}
.brand:hover { text-decoration: none; }
.brand-mark {
  align-items: center;
  background: var(--brand-background);
  color: #ffffff;
  display: inline-flex;
  font-size: 0.72rem;
  height: 32px;
  justify-content: center;
  width: 32px;
}
.navbar-spacer { flex: 1; }
.search {
  align-items: center;
  background: var(--surface-muted);
  border: 1px solid transparent;
  display: flex;
  flex: 0 1 220px;
  gap: 0.35rem;
  min-width: 0;
  padding: 0.35rem 0.65rem;
}
.search:focus-within { border-color: var(--primary); }
.search svg {
  fill: none;
  height: 16px;
  stroke: var(--muted);
  stroke-linecap: round;
  stroke-width: 2;
  width: 16px;
}
.search input {
  background: transparent;
  border: 0;
  color: var(--text);
  flex: 1;
  font: inherit;
  min-width: 0;
  outline: 0;
  width: 100%;
}
.search input::placeholder { color: var(--muted); }
.theme-button {
  align-items: center;
  background: transparent;
  border: 0;
  color: var(--text);
  cursor: pointer;
  display: inline-flex;
  height: 36px;
  justify-content: center;
  padding: 0;
  width: 36px;
}
.theme-button:hover { color: var(--primary); }
.theme-button:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }
.theme-icon {
  fill: none;
  height: 20px;
  stroke: currentColor;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-width: 2;
  width: 20px;
}
.theme-icon-sun { display: none; }
:root[data-theme="dark"] .theme-icon-sun { display: inline; }
:root[data-theme="dark"] .theme-icon-moon { display: none; }
.menu-button, .brand, .theme-button, .search svg { flex-shrink: 0; }
.menu-button {
  background: transparent;
  border: 0;
  color: var(--text);
  cursor: pointer;
  display: none;
  font-size: 1.5rem;
}
.page-layout {
  display: flex;
  min-height: calc(100vh - var(--navbar-height));
  min-width: 0;
}
.sidebar {
  background: var(--surface);
  border-right: 1px solid var(--border);
  flex: 0 0 var(--sidebar-width);
  height: calc(100vh - var(--navbar-height));
  overflow-y: auto;
  padding: 1.2rem 0.8rem 2rem;
  position: sticky;
  top: var(--navbar-height);
}
.sidebar a, .sidebar summary {
  color: var(--sidebar-text);
  display: block;
  line-height: 1.25;
  padding: 0.42rem 0.7rem;
}
.sidebar a:hover { background: var(--surface-muted); text-decoration: none; }
.sidebar a.active {
  background: var(--active-background);
  color: var(--primary-dark);
  font-weight: 700;
}
.sidebar summary {
  cursor: pointer;
  font-weight: 700;
  list-style-position: outside;
}
.sidebar-group { margin-top: 0.4rem; }
.sidebar-group-content { border-left: 1px solid var(--border); margin-left: 0.65rem; padding-left: 0.45rem; }
.sidebar-category { margin: 0.2rem 0; }
.sidebar-category summary { font-size: 0.92rem; }
.sidebar ul { list-style: none; margin: 0; padding: 0 0 0 0.45rem; }
.sidebar li { font-size: 0.9rem; }
.content-layout {
  display: grid;
  flex: 1;
  gap: 3rem;
  grid-template-columns: minmax(0, 850px) fit-content(320px);
  justify-content: center;
  min-width: 0;
  padding: 0 2.5rem;
}
.doc { min-width: 0; padding: 1.25rem 0 5rem; }
.doc h1 { font-size: 2.5rem; line-height: 1.2; margin: 1.4rem 0 1.6rem; }
.doc h2 { border-top: 1px solid var(--border); font-size: 1.8rem; margin-top: 3rem; padding-top: 1.5rem; }
.doc h3 { font-size: 1.35rem; margin-top: 2.2rem; }
.doc h4 { font-size: 1.05rem; margin-bottom: 0.5rem; }
.breadcrumbs { color: var(--muted); font-size: 0.88rem; }
.doc, .breadcrumbs, .sidebar a, .sidebar summary { overflow-wrap: anywhere; }
.breadcrumb-separator { margin: 0 0.5rem; }
.table-of-contents {
  align-self: start;
  border-left: 1px solid var(--border);
  color: var(--muted);
  font-size: 0.82rem;
  margin-top: 2.2rem;
  max-height: calc(100vh - 100px);
  max-width: 320px;
  min-width: 220px;
  overflow-y: auto;
  padding-left: 1rem;
  position: sticky;
  top: 85px;
}
.table-of-contents ul { list-style: none; margin: 0; padding: 0; }
.table-of-contents li { margin: 0.3rem 0; }
.table-of-contents .toc-level-3 { padding-left: 0.8rem; }
.table-of-contents a { color: var(--muted); overflow-wrap: anywhere; }
code {
  background: var(--inline-code-background);
  font-size: 0.92em;
  padding: 0.12rem 0.32rem;
}
pre {
  background: var(--code-background);
  color: var(--code-text);
  overflow-x: auto;
  padding: 1rem 1.2rem;
}
pre code { background: none; padding: 0; }
.optional-marker::after {
  content: "?";
  -webkit-user-select: none;
  user-select: none;
}
table {
  border-collapse: collapse;
  display: block;
  margin-bottom: 1.2rem;
  max-width: 100%;
  overflow-x: auto;
  width: max-content;
}
th, td {
  border: 1px solid var(--border);
  padding: 0.5rem 0.75rem;
  text-align: left;
  vertical-align: top;
}
th { background: var(--surface-muted); }
blockquote {
  background: var(--blockquote-background);
  border-left: 5px solid var(--primary);
  margin-left: 0;
  padding: 0.55rem 1rem;
}
blockquote p { margin: 0.4rem 0; }
@media (max-width: 1200px) {
  .content-layout { grid-template-columns: minmax(0, 850px); }
  .table-of-contents { display: none; }
}
@media (max-width: 996px) {
  .menu-button { display: block; }
  .sidebar {
    bottom: 0;
    left: 0;
    position: fixed;
    top: var(--navbar-height);
    transform: translateX(-105%);
    transition: transform 160ms ease;
    z-index: 15;
  }
  .sidebar-open .sidebar { transform: translateX(0); }
  .content-layout { padding: 0 1.4rem; width: 100%; }
}
@media (max-width: 600px) {
  .navbar { gap: 0.6rem; padding: 0 0.75rem; }
  .brand span:last-child, .navbar-spacer { display: none; }
  .search { flex: 1 1 auto; }
  .content-layout { padding: 0 1rem; }
  .doc h1 { font-size: 2rem; }
}
"""
