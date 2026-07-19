from __future__ import annotations

from collections import Counter
from html import escape, unescape
from html.parser import HTMLParser
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import markdown
from pygments.formatters import HtmlFormatter

from render_context import (
    CATEGORY_DIRECTORIES,
    CATEGORY_TITLES,
    RenderContext,
)


TOC_EXCLUDED_SECTIONS = {"constants", "fields", "members", "operations"}
SITE_ASSETS_PATH = Path(__file__).parent / "content" / "site"
HTML_TEMPLATE = (SITE_ASSETS_PATH / "page.html").read_text(encoding="utf-8")
THEME_SCRIPT = (SITE_ASSETS_PATH / "theme.js").read_text(encoding="utf-8")
SCRIPT = (SITE_ASSETS_PATH / "script.js").read_text(encoding="utf-8")
STYLE = (SITE_ASSETS_PATH / "style.css").read_text(encoding="utf-8")


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


class HtmlRenderer(RenderContext):
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
                category_directory = environment_directory / CATEGORY_DIRECTORIES[kind]
                category_active = current_markdown.is_relative_to(category_directory)
                category_open = " open" if category_active else ""
                output.append(
                    f'<details class="sidebar-category" '
                    f'data-sidebar-key="environment:{escape(environment.name)}:'
                    f'category:{kind}"{category_open}>'
                )
                output.append(
                    f"<summary>{escape(CATEGORY_TITLES[kind])}</summary>"
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
                include_children = anchor not in TOC_EXCLUDED_SECTIONS
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
            f"{STYLE}\n{light_highlight_style}\n{dark_highlight_style}\n",
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
                HTML_TEMPLATE.format(
                    title=escape(title or "Scrap Mechanic API"),
                    stylesheet=Path(stylesheet).as_posix(),
                    home=Path(home).as_posix(),
                    sidebar=self._sidebar(markdown_path, html_path),
                    breadcrumbs=self._breadcrumbs(markdown_path, html_path),
                    body=body,
                    toc=self._table_of_contents(body),
                    theme_script=THEME_SCRIPT,
                    script=SCRIPT,
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
