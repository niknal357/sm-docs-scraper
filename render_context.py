from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

from make_ir import Documentation, Environment, Page
from symbol_catalog import CATEGORY_DIRECTORIES, SymbolCatalog


CATEGORY_TITLES = {
    "namespace": "Static Functions",
    "userdata": "Userdata",
    "class": "Classes",
}


class RenderContext:
    def __init__(self, docs: Documentation, markdown_root: Path, html_root: Path):
        self.docs = docs
        self.markdown_root = markdown_root
        self.html_root = html_root
        self.symbol_catalog = SymbolCatalog(docs)
        self.page_paths: dict[int, Path] = {}
        self.page_details: dict[Path, tuple[Environment, str, Page]] = {}
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
                    self.page_details[path] = (environment, kind, page)
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
                            (path, self.symbol_catalog.slug(entry.name)),
                        )

                    if kind == "class":
                        for callback in self.symbol_catalog.callback_groups(page):
                            references[f"{page.name}.{callback.name}"] = (
                                path,
                                self.symbol_catalog.slug(callback.name),
                            )

                    if page.name == "GLOBAL":
                        for entry in page.constants + page.functions:
                            references.setdefault(
                                entry.name,
                                (path, self.symbol_catalog.slug(entry.name)),
                            )

    def _page_groups(
        self, environment: Environment
    ) -> Iterable[tuple[str, list[Page]]]:
        return self.symbol_catalog.page_groups(environment)

    def _navigation_groups(
        self, environment: Environment
    ) -> list[tuple[str, list[Page]]]:
        return sorted(
            self._page_groups(environment),
            key=lambda group: CATEGORY_TITLES[group[0]].casefold(),
        )

    def _environment_directory(self, environment: Environment) -> str:
        return self.symbol_catalog.environment_directory(environment)

    def _page_path(self, environment: Environment, kind: str, page: Page) -> Path:
        return self.markdown_root / self.symbol_catalog.page_path(
            environment, kind, page
        )

    def _class_template_path(self, page: Page) -> Path:
        return self.page_paths[id(page)].with_name(f"{page.name}-Template.md")

    @staticmethod
    def _page_sort_key(page: Page) -> str:
        return page.name.casefold()

    @staticmethod
    def _page_display_name(page: Page) -> str:
        return "Global" if page.name == "GLOBAL" else page.name

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
