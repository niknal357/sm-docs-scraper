from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from hashlib import sha1
from itertools import combinations
from pathlib import Path
import re
from typing import Iterable

from make_ir import Doc, Documentation, Entry, Environment, Inline, Page, Parameter


SIGNATURE_LINE_LENGTH = 80
ENVIRONMENT_DIRECTORIES = {
    "Game": "Game-Script-Environment",
    "Terrain": "Terrain-Script-Environment",
}
CATEGORY_DIRECTORIES = {
    "namespace": "Static-Functions",
    "userdata": "Userdata",
    "class": "Classes",
}
BINARY_OPERATORS = {
    "__add": "+",
    "__div": "/",
    "__eq": "==",
    "__lt": "<",
    "__mul": "*",
    "__sub": "-",
}
PRIMITIVE_TYPES = {
    "any",
    "boolean",
    "function",
    "integer",
    "nil",
    "number",
    "string",
    "table",
    "thread",
    "userdata",
}


@dataclass
class CallbackGroup:
    name: str
    server: Entry | None = None
    client: Entry | None = None

    @property
    def entries(self) -> tuple[Entry, ...]:
        return tuple(entry for entry in (self.server, self.client) if entry)


@dataclass(frozen=True)
class MethodAnchor:
    anchor: str
    label: str
    legacy_alias: str | None = None


@dataclass(frozen=True)
class Symbol:
    id: str
    environment: str
    page_kind: str
    page_name: str
    kind: str
    name: str
    qualified_name: str
    aliases: tuple[str, ...]
    anchor: str | None
    url: str
    signatures: tuple[str, ...]
    summary: str
    availability: tuple[str, ...]
    parameter_types: tuple[str, ...]
    return_types: tuple[str, ...]
    page: Page = field(repr=False, compare=False)
    entries: tuple[Entry, ...] = field(repr=False, compare=False)


class SymbolCatalog:
    def __init__(self, docs: Documentation):
        self.docs = docs
        self._page_kinds: dict[int, str] = {}
        self._callbacks: dict[int, tuple[CallbackGroup, ...]] = {}
        self._method_anchors: dict[int, dict[int, MethodAnchor]] = {}

        for _, kind, page in self.pages():
            self._page_kinds[id(page)] = kind
            self._callbacks[id(page)] = tuple(self._build_callback_groups(page))
            self._method_anchors[id(page)] = self._build_method_anchors(
                page, page.functions
            )

        self.symbols = tuple(self._build_symbols())

    @staticmethod
    def page_groups(
        environment: Environment,
    ) -> tuple[tuple[str, list[Page]], ...]:
        return (
            ("namespace", environment.namespaces),
            ("userdata", environment.userdata),
            ("class", environment.classes),
        )

    @staticmethod
    def environment_directory(environment: Environment) -> str:
        return ENVIRONMENT_DIRECTORIES.get(
            environment.name, f"{environment.name}-Script-Environment"
        )

    @classmethod
    def page_path(cls, environment: Environment, kind: str, page: Page) -> Path:
        filename = "Global" if page.name == "GLOBAL" else page.name
        return (
            Path(cls.environment_directory(environment))
            / CATEGORY_DIRECTORIES[kind]
            / f"{filename}.md"
        )

    @classmethod
    def symbol_url(
        cls,
        environment: Environment,
        kind: str,
        page: Page,
        anchor: str | None,
    ) -> str:
        path = cls.page_path(environment, kind, page).with_suffix(".html").as_posix()
        return f"{path}#{anchor}" if anchor else path

    def pages(self) -> Iterable[tuple[Environment, str, Page]]:
        for environment in self.docs.environments:
            for kind, pages in self.page_groups(environment):
                for page in pages:
                    yield environment, kind, page

    @staticmethod
    def slug(name: str) -> str:
        return re.sub(r"[^a-z0-9_-]+", "-", name.lower()).strip("-")

    @staticmethod
    def inline_text(content: Inline) -> str:
        return "".join(
            part
            if isinstance(part, str)
            else part.get("label", part["reference"])
            for part in content
        )

    @staticmethod
    def split_inline(content: Inline, delimiter: str = ",") -> list[Inline]:
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

    @staticmethod
    def instance_name(type_name: str) -> str:
        return type_name[:1].lower() + type_name[1:]

    def page_kind(self, page: Page) -> str:
        return self._page_kinds[id(page)]

    def callback_groups(self, page: Page) -> tuple[CallbackGroup, ...]:
        return self._callbacks[id(page)]

    @staticmethod
    def _build_callback_groups(page: Page) -> list[CallbackGroup]:
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

    def entry_parameters(self, page: Page, entry: Entry) -> list:
        if entry.doc is None:
            return []

        parameters = entry.doc.parameters
        kind = self.page_kind(page)
        if kind == "class" and parameters and parameters[0].name == "self":
            return parameters[1:]
        if kind == "userdata" and parameters:
            first_type = parameters[0].type
            if first_type == [{"reference": page.name}]:
                return parameters[1:]
        return parameters

    def method_anchors(self, page: Page) -> dict[int, MethodAnchor]:
        return self._method_anchors[id(page)]

    def method_anchor(self, page: Page, entry: Entry) -> MethodAnchor:
        return self._method_anchors[id(page)][id(entry)]

    @staticmethod
    def _minimum_unique_columns(rows: list[list[object]]) -> tuple[int, ...] | None:
        if not rows or not rows[0]:
            return None

        varying = [
            index
            for index in range(len(rows[0]))
            if len({row[index] for row in rows}) > 1
        ]
        for size in range(1, len(varying) + 1):
            for columns in combinations(varying, size):
                keys = {tuple(row[index] for index in columns) for row in rows}
                if len(keys) == len(rows):
                    return columns
        return None

    def _parameter_key(self, parameter: Parameter | None) -> object:
        if parameter is None:
            return None
        return self.inline_text(parameter.type), parameter.optional

    def _named_discriminators(
        self, parameter_rows: list[list[Parameter]]
    ) -> list[list[Parameter]] | None:
        parameter_maps = []
        for parameters in parameter_rows:
            counts = Counter(parameter.name for parameter in parameters)
            parameter_maps.append(
                {
                    parameter.name: parameter
                    for parameter in parameters
                    if counts[parameter.name] == 1
                }
            )

        common_names = set.intersection(
            *(set(parameters) for parameters in parameter_maps)
        )
        ordered_names = [
            parameter.name
            for parameter in parameter_rows[0]
            if parameter.name in common_names
        ]
        key_rows = [
            [self._parameter_key(parameters[name]) for name in ordered_names]
            for parameters in parameter_maps
        ]
        columns = self._minimum_unique_columns(key_rows)
        if columns is None:
            return None
        return [
            [parameters[ordered_names[index]] for index in columns]
            for parameters in parameter_maps
        ]

    def _positional_discriminators(
        self, parameter_rows: list[list[Parameter]]
    ) -> list[list[Parameter | None]] | None:
        width = max((len(parameters) for parameters in parameter_rows), default=0)
        padded_rows = [
            [
                parameters[index] if index < len(parameters) else None
                for index in range(width)
            ]
            for parameters in parameter_rows
        ]
        key_rows = [
            [self._parameter_key(parameter) for parameter in parameters]
            for parameters in padded_rows
        ]
        columns = self._minimum_unique_columns(key_rows)
        if columns is None:
            return None
        return [
            [parameters[index] for index in columns]
            for parameters in padded_rows
        ]

    def _discriminator_label(
        self,
        parameters: list[Parameter | None],
        argument_count: int,
        primitive_names: bool,
        optional_markers: bool,
    ) -> str:
        parts = []
        for parameter in parameters:
            if parameter is None:
                part = (
                    "no arguments"
                    if argument_count == 0
                    else f"{argument_count} "
                    f"{'argument' if argument_count == 1 else 'arguments'}"
                )
            else:
                type_name = self.inline_text(parameter.type)
                use_name = (
                    primitive_names
                    and type_name.casefold() in PRIMITIVE_TYPES
                    and len(parameter.name) > 1
                )
                part = parameter.name if use_name else type_name
                if optional_markers and parameter.optional:
                    part += "?"
            if part not in parts:
                parts.append(part)
        return " + ".join(parts)

    def _overload_labels(
        self, page: Page, entries: list[Entry]
    ) -> dict[int, str]:
        parameter_rows = [self.entry_parameters(page, entry) for entry in entries]
        named = self._named_discriminators(parameter_rows)
        positional = self._positional_discriminators(parameter_rows)

        if named is not None and (
            positional is None or len(named[0]) <= len(positional[0])
        ):
            discriminators = named
        else:
            discriminators = positional
        if discriminators is None:
            return {}

        attempts = (
            (True, False),
            (False, False),
            (True, True),
            (False, True),
        )
        for primitive_names, optional_markers in attempts:
            labels = [
                self._discriminator_label(
                    parameters,
                    len(parameter_rows[index]),
                    primitive_names,
                    optional_markers,
                )
                for index, parameters in enumerate(discriminators)
            ]
            if len({label.casefold() for label in labels}) == len(labels):
                return {
                    id(entry): f"{entry.name} - {label}"
                    for entry, label in zip(entries, labels, strict=True)
                }
        return {}

    def _build_method_anchors(
        self, page: Page, entries: list[Entry]
    ) -> dict[int, MethodAnchor]:
        groups: dict[str, list[Entry]] = {}
        for entry in entries:
            groups.setdefault(self.slug(entry.name), []).append(entry)
        overload_labels = {
            entry_id: label
            for group in groups.values()
            if len(group) > 1
            for entry_id, label in self._overload_labels(page, group).items()
        }

        used: set[str] = set()
        first_overload: set[str] = set()
        anchors: dict[int, MethodAnchor] = {}

        for entry in entries:
            base = self.slug(entry.name)
            if len(groups[base]) == 1:
                anchors[id(entry)] = MethodAnchor(anchor=base, label=entry.name)
                used.add(base)
                continue

            parameters = self.entry_parameters(page, entry)
            display_types = [
                self.inline_text(parameter.type)
                + ("?" if parameter.optional else "")
                for parameter in parameters
            ]
            label = overload_labels.get(
                id(entry), f"{entry.name}({', '.join(display_types)})"
            )
            suffix_parts = []
            for parameter in parameters:
                type_slug = self.slug(self.inline_text(parameter.type)) or "any"
                if parameter.optional:
                    type_slug += "-optional"
                suffix_parts.append(type_slug)
            suffix = "-".join(suffix_parts) or "no-arguments"
            candidate = f"{base}-{suffix}"

            if candidate in used:
                detailed_signature = ",".join(
                    f"{parameter.name}:{self.inline_text(parameter.type)}:"
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

    def signature(self, page: Page, entry: Entry) -> str:
        if entry.doc is None:
            return entry.name

        kind = self.page_kind(page)
        parameters = self.entry_parameters(page, entry)
        names = [
            f"{parameter.name}?" if parameter.optional else parameter.name
            for parameter in parameters
        ]
        arguments = ", ".join(names)

        if kind == "namespace":
            prefix = "" if page.name == "GLOBAL" else f"{page.name}."
        elif kind == "userdata":
            prefix = f"{self.instance_name(page.name)}:"
        else:
            prefix = f"{page.name}:"

        signature = f"{prefix}{entry.name}( {arguments} )"
        if len(signature) <= SIGNATURE_LINE_LENGTH or not names:
            return signature

        lines = [f"{prefix}{entry.name}("]
        lines.extend(
            f"    {name}{',' if index < len(names) - 1 else ''}"
            for index, name in enumerate(names)
        )
        lines.append(")")
        return "\n".join(lines)

    def operation_signature(self, name: str, signature: Inline) -> tuple[str, Inline]:
        parts = self.split_inline(signature)
        if name in BINARY_OPERATORS and len(parts) == 3:
            left = self.inline_text(parts[0])
            right = self.inline_text(parts[1])
            return f"{left} {BINARY_OPERATORS[name]} {right}", parts[2]
        if name == "__unm" and len(parts) == 2:
            return f"-{self.inline_text(parts[0])}", parts[1]
        if name == "__tostring" and len(parts) == 2:
            return f"tostring({self.inline_text(parts[0])})", parts[1]
        raise ValueError(f"Unsupported operation signature: {name}")

    def member_type(self, page: Page, member: Entry) -> Inline:
        if member.get and member.get.returns:
            return member.get.returns[0].type

        if member.set and member.set.parameters:
            parameters = member.set.parameters
            if parameters[0].type == [{"reference": page.name}]:
                parameters = parameters[1:]
            if parameters:
                return parameters[-1].type

        return ["unknown"]

    def _build_symbols(self) -> Iterable[Symbol]:
        for environment, page_kind, page in self.pages():
            yield self._symbol(
                environment,
                page_kind,
                page,
                "page",
                page.name,
                None,
                (),
            )

            for entry in page.constants:
                yield self._symbol(
                    environment,
                    page_kind,
                    page,
                    "constant",
                    entry.name,
                    self.slug(entry.name),
                    (entry,),
                )

            for entry in page.functions:
                yield self._symbol(
                    environment,
                    page_kind,
                    page,
                    "function",
                    entry.name,
                    self.method_anchor(page, entry).anchor,
                    (entry,),
                    signatures=(self.signature(page, entry),),
                )

            for member in page.members:
                yield self._symbol(
                    environment,
                    page_kind,
                    page,
                    "member",
                    member.name,
                    self.slug(member.name),
                    (member,),
                )

            for entry in page.metamethods:
                signatures = tuple(
                    self.operation_signature(entry.name, operation.signature)[0]
                    for operation in (entry.doc.operations if entry.doc else [])
                )
                yield self._symbol(
                    environment,
                    page_kind,
                    page,
                    "operation",
                    entry.name,
                    self.slug(entry.name),
                    (entry,),
                    signatures=signatures,
                )

            for callback in self.callback_groups(page):
                yield self._symbol(
                    environment,
                    page_kind,
                    page,
                    "callback",
                    callback.name,
                    self.slug(callback.name),
                    callback.entries,
                    signatures=tuple(
                        self.signature(page, entry) for entry in callback.entries
                    ),
                )

    def _symbol(
        self,
        environment: Environment,
        page_kind: str,
        page: Page,
        symbol_kind: str,
        name: str,
        anchor: str | None,
        entries: tuple[Entry, ...],
        signatures: tuple[str, ...] = (),
    ) -> Symbol:
        qualified_name = self._qualified_name(page_kind, page, symbol_kind, name)
        aliases = self._aliases(page, symbol_kind, name, qualified_name, entries)
        docs = tuple(self._entry_docs(entries))
        if symbol_kind == "page" and page.doc:
            docs = (page.doc,)

        stable_anchor = anchor or "page"
        stable_id = ":".join(
            (environment.name, page_kind, page.name, symbol_kind, stable_anchor)
        )
        return Symbol(
            id=stable_id,
            environment=environment.name,
            page_kind=page_kind,
            page_name=page.name,
            kind=symbol_kind,
            name=name,
            qualified_name=qualified_name,
            aliases=aliases,
            anchor=anchor,
            url=self.symbol_url(environment, page_kind, page, anchor),
            signatures=signatures,
            summary=self._summary(docs),
            availability=self._availability(docs),
            parameter_types=self._parameter_types(page, entries),
            return_types=self._return_types(entries),
            page=page,
            entries=entries,
        )

    @staticmethod
    def _qualified_name(
        page_kind: str, page: Page, symbol_kind: str, name: str
    ) -> str:
        if symbol_kind == "page":
            return "Global" if page.name == "GLOBAL" else page.name
        if page.name == "GLOBAL":
            return name
        separator = (
            ":"
            if symbol_kind in {"function", "callback"}
            and page_kind != "namespace"
            else "."
        )
        return f"{page.name}{separator}{name}"

    def _aliases(
        self,
        page: Page,
        symbol_kind: str,
        name: str,
        qualified_name: str,
        entries: tuple[Entry, ...],
    ) -> tuple[str, ...]:
        values = [name, qualified_name]
        if symbol_kind == "page" and page.name == "GLOBAL":
            values.append(page.name)
        if symbol_kind == "callback":
            values.extend(entry.name for entry in entries)
            values.extend(f"{page.name}:{entry.name}" for entry in entries)

        aliases: list[str] = []
        for value in values:
            word_alias = self._identifier_words(value)
            variants = (
                value,
                word_alias,
                re.sub(r"raycast", "ray cast", word_alias, flags=re.IGNORECASE),
            )
            for alias in variants:
                if alias and alias not in aliases:
                    aliases.append(alias)
        return tuple(aliases)

    @staticmethod
    def _identifier_words(value: str) -> str:
        separated = re.sub(r"[._:]", " ", value)
        separated = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", separated)
        return " ".join(separated.split())

    @staticmethod
    def _entry_docs(entries: tuple[Entry, ...]) -> Iterable[Doc]:
        for entry in entries:
            for doc in (entry.doc, entry.get, entry.set):
                if doc:
                    yield doc

    def _summary(self, docs: tuple[Doc, ...]) -> str:
        for doc in docs:
            for block in doc.content:
                if block["type"] == "paragraph":
                    return self.inline_text(block["content"]).strip()
        return ""

    @staticmethod
    def _availability(docs: tuple[Doc, ...]) -> tuple[str, ...]:
        return tuple(dict.fromkeys(doc.availability for doc in docs))

    def _parameter_types(
        self, page: Page, entries: tuple[Entry, ...]
    ) -> tuple[str, ...]:
        values: list[str] = []
        for entry in entries:
            if entry.doc:
                parameters = self.entry_parameters(page, entry)
                values.extend(
                    self.inline_text(parameter.type) for parameter in parameters
                )
            if entry.set:
                values.extend(
                    self.inline_text(parameter.type)
                    for parameter in entry.set.parameters
                )
        return tuple(dict.fromkeys(values))

    def _return_types(self, entries: tuple[Entry, ...]) -> tuple[str, ...]:
        values: list[str] = []
        for entry in entries:
            for doc in (entry.doc, entry.get):
                if doc:
                    values.extend(
                        self.inline_text(return_value.type)
                        for return_value in doc.returns
                    )
        return tuple(dict.fromkeys(values))
