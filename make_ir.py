from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
import json
from pathlib import Path
import re
import textwrap
from typing import Any


_REFERENCE = re.compile(r"\[([^\[\]]+)]")
_REFERENCE_TARGET = re.compile(r"^[A-Za-z_][A-Za-z0-9_.]*$")
_SOURCE_TEXT_CORRECTIONS = {
    "(See[sm.shape.destructionType)": "(See [sm.shape.destructionType])",
}
_BLOCK_MARKERS = {
    "@code": "code",
    "@list": "list",
    "@note": "note",
    "@table": "table",
    "@warning": "warning",
}

Inline = list[str | dict[str, str]]


@dataclass
class Parameter:
    name: str
    type: Inline
    description: Inline
    optional: bool = False


@dataclass
class ReturnValue:
    type: Inline
    description: Inline
    name: str | None = None


@dataclass
class Field:
    name: str
    type: Inline
    description: Inline


@dataclass
class MetaOperation:
    signature: Inline
    description: Inline


@dataclass
class Doc:
    content: list[dict[str, Any]] = field(default_factory=list)
    parameters: list[Parameter] = field(default_factory=list)
    returns: list[ReturnValue] = field(default_factory=list)
    fields: list[Field] = field(default_factory=list)
    operations: list[MetaOperation] = field(default_factory=list)
    availability: str = "server and client"
    deprecated: list[dict[str, Any]] = field(default_factory=list)
    hidden: bool = False


@dataclass
class Entry:
    name: str
    doc: Doc | None = None
    callback_type: str | None = None
    get: Doc | None = None
    set: Doc | None = None


@dataclass
class Page:
    name: str
    source: str
    associated_type: str | None = None
    associated_namespace: str | None = None
    usage: str | None = None
    serializable: bool | None = None
    doc: Doc | None = None
    constants: list[Entry] = field(default_factory=list)
    functions: list[Entry] = field(default_factory=list)
    members: list[Entry] = field(default_factory=list)
    metamethods: list[Entry] = field(default_factory=list)
    common_callbacks: list[Entry] = field(default_factory=list)
    callbacks: list[Entry] = field(default_factory=list)


@dataclass
class Environment:
    name: str
    namespaces: list[Page] = field(default_factory=list)
    userdata: list[Page] = field(default_factory=list)
    classes: list[Page] = field(default_factory=list)


@dataclass
class Documentation:
    version: int
    environments: list[Environment]


def parse_inline(text: str) -> Inline:
    parts: Inline = []
    offset = 0

    for match in _REFERENCE.finditer(text):
        raw_reference = match.group(1)
        target, separator, label = raw_reference.partition(",")
        target = target.strip()

        if not _REFERENCE_TARGET.fullmatch(target):
            continue

        if match.start() > offset:
            parts.append(text[offset : match.start()])

        reference = {"reference": target}
        if separator and label.strip() != target:
            reference["label"] = label.strip()
        parts.append(reference)
        offset = match.end()

    if offset < len(text):
        parts.append(text[offset:])

    return parts


def parse_blocks(lines: list[str]) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    index = 0

    while index < len(lines):
        line = lines[index]
        block_type = _BLOCK_MARKERS.get(line)

        if block_type is None:
            blocks.append({"type": "paragraph", "content": parse_inline(line)})
            index += 1
            continue

        end = index + 1
        while end < len(lines) and lines[end] != line:
            end += 1
        if end == len(lines):
            raise ValueError(f"Unclosed {line} block")

        contents = lines[index + 1 : end]
        if block_type == "code":
            if contents:
                contents = textwrap.dedent("\n".join(contents)).split("\n")
            block = {"type": "code", "language": "lua", "lines": contents}
        elif block_type == "list":
            block = {"type": "list", "items": [parse_inline(item) for item in contents]}
        elif block_type == "table":
            block = {
                "type": "table",
                "rows": [
                    [parse_inline(cell.strip()) for cell in row.split(";")]
                    for row in contents
                ],
            }
        else:
            block = {
                "type": block_type,
                "content": [parse_inline(item) for item in contents],
            }

        blocks.append(block)
        index = end + 1

    return blocks


def _availability(raw: dict[str, Any]) -> str:
    server_only = raw.get("server_only", False)
    client_only = raw.get("client_only", False)
    if server_only and client_only:
        raise ValueError("A document cannot be both server-only and client-only")
    if server_only:
        return "server"
    if client_only:
        return "client"
    return "server and client"


def _text_columns(text: str) -> list[str]:
    return [
        column.strip()
        for column in re.split(r"\t+", text)
        if column.strip()
    ]


def _normalize_description(description: str) -> str:
    columns = _text_columns(description)
    if not columns:
        return ""
    normalized = re.sub(r"\s+", " ", columns[-1]).strip()
    for source, replacement in _SOURCE_TEXT_CORRECTIONS.items():
        normalized = normalized.replace(source, replacement)
    return normalized


def _is_return_name(value: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", value))


def _parse_return(type_name: str, description: str) -> ReturnValue:
    name = None
    if not description.strip() and "\t" in type_name:
        columns = _text_columns(type_name)
        if len(columns) > 1:
            type_name = columns[0]
            remainder = columns[1:]
            if _is_return_name(remainder[0]):
                name = remainder[0]
                description = remainder[-1] if len(remainder) > 1 else ""
            else:
                description = remainder[-1]
    elif "\t" in description:
        columns = _text_columns(description)
        if len(columns) > 1 and _is_return_name(columns[0]):
            name = columns[0]
            description = columns[-1]

    type_name = re.sub(r"\s+", " ", type_name).strip()
    description = _normalize_description(description)
    if name is None and _is_return_name(description):
        name = description
        description = ""

    return ReturnValue(
        type=parse_inline(type_name),
        description=parse_inline(description),
        name=name,
    )


def parse_doc(raw: dict[str, Any]) -> Doc:
    parameters = []
    for type_name, name, description in raw.get("params", []):
        optional = name.endswith("?")
        parameters.append(
            Parameter(
                name=name.removesuffix("?"),
                type=parse_inline(type_name),
                description=parse_inline(_normalize_description(description)),
                optional=optional,
            )
        )

    returns = [
        _parse_return(type_name, description)
        for type_name, description in raw.get("return", [])
    ]
    fields = [
        Field(
            name=name,
            type=parse_inline(type_name),
            description=parse_inline(_normalize_description(description)),
        )
        for type_name, name, description in raw.get("fields", [])
    ]
    operations = [
        MetaOperation(
            signature=parse_inline(signature),
            description=parse_inline(_normalize_description(description)),
        )
        for signature, description in raw.get("meta", [])
    ]

    return Doc(
        content=parse_blocks(raw.get("text", [])),
        parameters=parameters,
        returns=returns,
        fields=fields,
        operations=operations,
        availability=_availability(raw),
        deprecated=parse_blocks(raw.get("deprecated", [])),
        hidden=bool(raw.get("hidden", False)),
    )


def _parse_entries(raw: list[dict[str, Any]]) -> list[Entry]:
    return [Entry(name=item["name"], doc=parse_doc(item["doc"])) for item in raw]


def _parse_members(raw: list[dict[str, Any]]) -> list[Entry]:
    members = []
    for item in raw:
        members.append(
            Entry(
                name=item["name"],
                get=parse_doc(item["get"]["doc"]) if "get" in item else None,
                set=parse_doc(item["set"]["doc"]) if "set" in item else None,
            )
        )
    return members


def _parse_callbacks(raw: list[dict[str, Any]]) -> list[Entry]:
    return [
        Entry(
            name=item["name"],
            doc=parse_doc(item["doc"]),
            callback_type=item["type"],
        )
        for item in raw
    ]


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def _parse_page(path: Path, kind: str, expected_name: str) -> Page:
    raw = _load_json(path)
    name_key = {"namespace": "namespace", "userdata": "userdata", "class": "class"}[kind]
    name = raw[name_key]
    if name != expected_name:
        raise ValueError(f"{path}: expected {expected_name!r}, found {name!r}")

    return Page(
        name=name,
        source=path.name,
        associated_type=raw.get("userdata_association"),
        associated_namespace=raw.get("namespace_association"),
        usage=raw.get("usage"),
        serializable=raw.get("serializable"),
        doc=parse_doc(raw["doc"]),
        constants=_parse_entries(raw.get("constants", [])),
        functions=_parse_entries(raw.get("functions", [])),
        members=_parse_members(raw.get("members", [])),
        metamethods=_parse_entries(raw.get("metamethods", [])),
        common_callbacks=_parse_callbacks(raw.get("common_callbacks", [])),
        callbacks=_parse_callbacks(raw.get("callbacks", [])),
    )


def make_ir(json_dir: Path | str) -> Documentation:
    json_dir = Path(json_dir)
    index = _load_json(json_dir / "index.json")
    environments = []

    for environment_name, contents in index.items():
        environment = Environment(name=environment_name)

        for name in contents.get("namespaces", []):
            path = json_dir / f"namespace_{environment_name}_{name}.json"
            environment.namespaces.append(_parse_page(path, "namespace", name))

        for name in contents.get("userdata", []):
            path = json_dir / f"userdata_{environment_name}_{name}.json"
            environment.userdata.append(_parse_page(path, "userdata", name))

        for name in contents.get("classes", []):
            path = json_dir / f"class_{environment_name}_{name}.json"
            environment.classes.append(_parse_page(path, "class", name))

        environments.append(environment)

    return Documentation(version=1, environments=environments)


def _compact(value: Any) -> Any:
    if is_dataclass(value):
        value = asdict(value)
    if isinstance(value, dict):
        compacted_items = {}
        for key, item in value.items():
            if key in {"hidden", "optional"} and item is False:
                continue
            compacted = _compact(item)
            if compacted is not None:
                compacted_items[key] = compacted
        return compacted_items
    if isinstance(value, list):
        if not value:
            return None
        return [_compact(item) for item in value]
    if value is None:
        return None
    return value


def write_ir(ir: Documentation, output_dir: Path | str) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "docs.json"
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(_compact(ir), file, indent=2, ensure_ascii=False)
        file.write("\n")
    return output_path
