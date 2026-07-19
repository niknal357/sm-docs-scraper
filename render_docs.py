from __future__ import annotations

from html import escape
import os
from pathlib import Path
import re
import shutil
from typing import Iterable

import markdown

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
                        references[f"{page.name}.{entry.name}"] = (
                            path,
                            self._slug(entry.name),
                        )

                    if page.name == "GLOBAL":
                        for entry in page.constants + page.functions:
                            references[entry.name] = (path, self._slug(entry.name))

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

        self._write_html_tree()
        return self.markdown_root, self.html_root

    @staticmethod
    def _page_groups(environment: Environment) -> Iterable[tuple[str, list[Page]]]:
        return (
            ("namespace", environment.namespaces),
            ("userdata", environment.userdata),
            ("class", environment.classes),
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

    @staticmethod
    def _slug(name: str) -> str:
        return re.sub(r"[^a-z0-9_-]+", "-", name.lower()).strip("-")

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
                rendered.append(part)
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
    ) -> list[str]:
        output: list[str] = []

        if doc.hidden:
            output.extend(["**Visibility:** Hidden", ""])
        if doc.availability != "server and client":
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

    def _signature(self, kind: str, page: Page, entry: Entry) -> str:
        if entry.doc is None:
            return entry.name

        parameters = entry.doc.parameters
        if kind == "class" and parameters and parameters[0].name == "self":
            parameters = parameters[1:]
        elif kind == "userdata" and parameters:
            first_type = parameters[0].type
            if first_type == [{"reference": page.name}]:
                parameters = parameters[1:]

        names = [
            f"{parameter.name}?" if parameter.optional else parameter.name
            for parameter in parameters
        ]
        arguments = ", ".join(names)

        if kind == "namespace":
            prefix = "" if page.name == "GLOBAL" else f"{page.name}."
        else:
            prefix = f"{page.name}:"
        return f"{prefix}{entry.name}( {arguments} )"

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
            output.extend(
                [
                    f'<a id="{self._slug(entry.name)}"></a>',
                    f"### `{entry.name}`",
                    "",
                ]
            )
            if title != "Constants":
                output.extend(
                    [
                        "```lua",
                        self._signature(kind, page, entry),
                        "```",
                        "",
                    ]
                )
            if entry.callback_type:
                output.extend(
                    [f"**Callback type:** `{entry.callback_type}`", ""]
                )
            if entry.doc:
                output.extend(self._doc(environment, current_path, entry.doc, 4))
        return output

    def _write_page(self, environment: Environment, kind: str, page: Page) -> None:
        path = self.page_paths[id(page)]
        path.parent.mkdir(parents=True, exist_ok=True)
        output = [f"# `{page.name}`", ""]

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

        if page.members:
            output.extend(["## Members", ""])
            for member in page.members:
                output.extend(
                    [
                        f'<a id="{self._slug(member.name)}"></a>',
                        f"### `{member.name}`",
                        "",
                    ]
                )
                if member.get:
                    output.extend(["#### Get", ""])
                    output.extend(self._doc(environment, path, member.get, 5))
                if member.set:
                    output.extend(["#### Set", ""])
                    output.extend(self._doc(environment, path, member.set, 5))

        output.extend(
            self._entries(
                environment, path, kind, page, "Operations", page.metamethods
            )
        )
        output.extend(
            self._entries(
                environment, path, kind, page, "Functions", page.functions
            )
        )
        output.extend(
            self._entries(
                environment,
                path,
                kind,
                page,
                "Common callbacks",
                page.common_callbacks,
            )
        )
        output.extend(
            self._entries(
                environment, path, kind, page, "Callbacks", page.callbacks
            )
        )

        path.write_text("\n".join(output).rstrip() + "\n", encoding="utf-8")

    def _write_markdown_index(self) -> None:
        output = ["# Scrap Mechanic API", ""]
        for environment in self.docs.environments:
            directory = self._environment_directory(environment)
            output.append(f"- [{environment.name}]({directory}/index.md)")
        output.append("")
        (self.markdown_root / "index.md").write_text(
            "\n".join(output), encoding="utf-8"
        )

    def _write_environment_index(self, environment: Environment) -> None:
        directory = self.markdown_root / self._environment_directory(environment)
        directory.mkdir(parents=True, exist_ok=True)
        output = [f"# {environment.name} script environment", ""]
        for kind, pages in self._page_groups(environment):
            if pages:
                category = _CATEGORY_DIRECTORIES[kind]
                output.append(f"- [{category}]({category}/index.md)")
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
        output = [f"# {_CATEGORY_DIRECTORIES[kind]}", ""]
        for page in pages:
            path = self.page_paths[id(page)]
            output.append(f"- [`{page.name}`]({path.name})")
        output.append("")
        (directory / "index.md").write_text("\n".join(output), encoding="utf-8")

    def _write_html_tree(self) -> None:
        self.html_root.mkdir(parents=True)
        assets = self.html_root / "assets"
        assets.mkdir()
        (assets / "style.css").write_text(_STYLE, encoding="utf-8")

        for markdown_path in self.markdown_root.rglob("*.md"):
            relative = markdown_path.relative_to(self.markdown_root)
            html_path = self.html_root / relative.with_suffix(".html")
            html_path.parent.mkdir(parents=True, exist_ok=True)
            body = markdown.markdown(
                markdown_path.read_text(encoding="utf-8"),
                extensions=["fenced_code", "tables", "sane_lists"],
            )
            body = re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', body)
            stylesheet = os.path.relpath(assets / "style.css", html_path.parent)
            home = os.path.relpath(self.html_root / "index.html", html_path.parent)
            title = relative.stem if relative.stem != "index" else relative.parent.name
            html_path.write_text(
                _HTML_TEMPLATE.format(
                    title=escape(title or "Scrap Mechanic API"),
                    stylesheet=Path(stylesheet).as_posix(),
                    home=Path(home).as_posix(),
                    body=body,
                ),
                encoding="utf-8",
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
  <title>{title}</title>
  <link rel="stylesheet" href="{stylesheet}">
</head>
<body>
  <nav><a href="{home}">API index</a></nav>
  <main>{body}</main>
</body>
</html>
"""

_STYLE = """body {
  color: #20232a;
  font: 16px/1.6 system-ui, sans-serif;
  margin: 0;
}
nav {
  background: #20232a;
  padding: 0.75rem 2rem;
}
nav a { color: white; }
main {
  margin: 0 auto;
  max-width: 1100px;
  padding: 1rem 2rem 4rem;
}
a { color: #087ea4; }
code {
  background: #f1f3f5;
  border-radius: 4px;
  padding: 0.1rem 0.3rem;
}
pre {
  background: #20232a;
  border-radius: 6px;
  color: #f8f9fa;
  overflow-x: auto;
  padding: 1rem;
}
pre code { background: none; padding: 0; }
table {
  border-collapse: collapse;
  display: block;
  margin-bottom: 1rem;
  overflow-x: auto;
  width: max-content;
  max-width: 100%;
}
th, td {
  border: 1px solid #ced4da;
  padding: 0.4rem 0.7rem;
  text-align: left;
  vertical-align: top;
}
blockquote {
  border-left: 4px solid #087ea4;
  margin-left: 0;
  padding: 0.1rem 1rem;
}
"""
