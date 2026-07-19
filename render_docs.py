from __future__ import annotations

from pathlib import Path
import shutil

from make_ir import Documentation
from render_html import HtmlRenderer
from render_markdown import MarkdownRenderer
from search_index import build_search_indexes


class DocumentationRenderer(MarkdownRenderer, HtmlRenderer):
    def render(self) -> tuple[Path, Path]:
        shutil.rmtree(self.markdown_root, ignore_errors=True)
        shutil.rmtree(self.html_root, ignore_errors=True)
        self.markdown_root.mkdir(parents=True)

        self._write_markdown_index()
        self._write_search_page()
        for environment in self.docs.environments:
            self._write_environment_index(environment)
            for kind, pages in self._page_groups(environment):
                self._write_category_index(environment, kind, pages)
                for page in pages:
                    self._write_page(environment, kind, page)
                    if kind == "class":
                        self._write_class_template(page)

        self._write_html_tree()
        build_search_indexes(self.symbol_catalog, self.html_root)
        self._validate_html_tree()
        return self.markdown_root, self.html_root


def render_docs(
    docs: Documentation,
    markdown_root: Path | str,
    html_root: Path | str,
) -> tuple[Path, Path]:
    renderer = DocumentationRenderer(
        docs, Path(markdown_root), Path(html_root)
    )
    return renderer.render()
