from __future__ import annotations

import os
import re
from collections.abc import Iterable
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from make_ir import Doc, Documentation, Environment, Page
from symbol_catalog import SymbolCatalog

CATEGORY_TITLES = {
    "namespace": "Static Functions",
    "userdata": "Userdata",
    "class": "Classes",
}
TYPE_CONTEXT_BEFORE = re.compile(
    r"(?:table|array|list|collection|set)\s+of\s+(?:an?\s+)?$",
    flags=re.IGNORECASE,
)
NAMESPACE_CONTEXT_BEFORE = re.compile(
    r"(?:see|visit)\s+(?:the\s+)?$",
    flags=re.IGNORECASE,
)
NAMESPACE_CONTEXT_AFTER = re.compile(
    r"^\s*(?:api|namespace|module|library|functions?)\b",
    flags=re.IGNORECASE,
)
DEFAULT_SITE_URL = "https://scrapmechanicdocs.com/"


class RenderContext:
    def __init__(
        self,
        docs: Documentation,
        markdown_root: Path,
        html_root: Path,
        previous_page_digests: dict | None = None,
    ):
        self.docs = docs
        self.markdown_root = markdown_root
        self.html_root = html_root
        self.previous_page_digests = previous_page_digests

        site_url = (
            os.environ.get("SM_DOCS_SITE_URL", "").strip() or DEFAULT_SITE_URL
        )
        try:
            parsed_site_url = urlsplit(site_url)
            hostname = parsed_site_url.hostname
            _ = parsed_site_url.port
        except ValueError as error:
            raise ValueError(
                "SM_DOCS_SITE_URL must be an absolute HTTP(S) base URL"
            ) from error
        if (
            parsed_site_url.scheme not in {"http", "https"}
            or not parsed_site_url.netloc
            or not hostname
            or parsed_site_url.username is not None
            or parsed_site_url.password is not None
            or parsed_site_url.query
            or parsed_site_url.fragment
            or any(character.isspace() for character in site_url)
        ):
            raise ValueError(
                "SM_DOCS_SITE_URL must be an absolute HTTP(S) base URL "
                "without credentials, a query, or a fragment"
            )
        site_path = parsed_site_url.path or "/"
        if not site_path.endswith("/"):
            site_path += "/"
        self.site_url = urlunsplit(
            (
                parsed_site_url.scheme,
                parsed_site_url.netloc,
                site_path,
                "",
                "",
            )
        )

        self.build_date = datetime.now(UTC).date().isoformat()

        self.symbol_catalog = SymbolCatalog(docs)
        self.page_paths: dict[int, Path] = {}
        self.page_details: dict[Path, tuple[Environment, str, Page]] = {}
        self.references: dict[str, dict[str, tuple[Path, str | None]]] = {}
        self.namespace_type_associations: dict[str, dict[str, str]] = {}
        self._index_references()

    def _index_references(self) -> None:
        for environment in self.docs.environments:
            references: dict[str, tuple[Path, str | None]] = {}
            self.references[environment.name] = references
            self.namespace_type_associations[environment.name] = {
                page.name: page.associated_type
                for page in environment.namespaces
                if page.associated_type
            }

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

    @staticmethod
    def _doc_has_source_content(doc: Doc | None) -> bool:
        return bool(
            doc
            and any(
                getattr(doc, attribute)
                for attribute in (
                    "content",
                    "parameters",
                    "returns",
                    "fields",
                    "operations",
                    "deprecated",
                )
            )
        )

    @classmethod
    def _page_has_source_content(cls, page: Page) -> bool:
        entries = (
            page.constants
            + page.functions
            + page.members
            + page.metamethods
            + page.common_callbacks
            + page.callbacks
        )
        return cls._doc_has_source_content(page.doc) or bool(entries)

    @staticmethod
    def _normalized_reference_label(label: str) -> str:
        return re.sub(r"[^a-z0-9]", "", label.casefold())

    @staticmethod
    def _pluralized_type_name(type_name: str) -> str:
        folded = type_name.casefold()
        if (
            folded.endswith("y")
            and len(type_name) > 1
            and folded[-2] not in "aeiou"
        ):
            return type_name[:-1] + "ies"
        if folded.endswith(("s", "x", "z", "ch", "sh")):
            return type_name + "es"
        return type_name + "s"

    @classmethod
    def _type_reference_labels(cls, type_name: str) -> set[str]:
        return {
            cls._normalized_reference_label(type_name),
            cls._normalized_reference_label(cls._pluralized_type_name(type_name)),
        }

    @classmethod
    def _associated_type_link_label(
        cls,
        type_name: str,
        source_label: str,
        *,
        explicit_label: bool,
    ) -> str:
        if not explicit_label:
            return type_name
        normalized_label = cls._normalized_reference_label(source_label)
        plural = cls._pluralized_type_name(type_name)
        if normalized_label == cls._normalized_reference_label(plural):
            return plural
        if normalized_label == cls._normalized_reference_label(type_name):
            return type_name
        return source_label

    @staticmethod
    def _inside_braced_type(prefix: str, suffix: str) -> bool:
        opening = prefix.rfind("{")
        return opening > prefix.rfind("}") and suffix.find("}") >= 0

    def _resolve_reference_target(
        self,
        environment: Environment,
        target: str,
        label: str,
        prefix: str,
        suffix: str,
        *,
        explicit_label: bool = False,
        type_context: bool = False,
    ) -> str:
        associated_type = self.namespace_type_associations[
            environment.name
        ].get(target)
        if (
            associated_type is None
            or associated_type not in self.references[environment.name]
        ):
            return target

        if (
            type_context
            or self._inside_braced_type(prefix, suffix)
            or TYPE_CONTEXT_BEFORE.search(prefix)
        ):
            return associated_type

        label_matches_type = (
            explicit_label
            and self._normalized_reference_label(label)
            in self._type_reference_labels(associated_type)
        )
        if not label_matches_type:
            return target

        namespace_context = NAMESPACE_CONTEXT_BEFORE.search(
            prefix
        ) or NAMESPACE_CONTEXT_AFTER.match(suffix)
        if namespace_context:
            return target
        return associated_type

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
