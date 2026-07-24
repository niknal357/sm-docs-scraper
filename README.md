# SM Docs Scraper

Downloads the Scrap Mechanic API documentation and generates Markdown and HTML documentation sites.

## Generate the site

```bash
uv run python main.py
```

Generated files:

- `temp/json/`: downloaded source documentation
- `temp/ir/docs.json`: normalized intermediate representation
- `dist/markdown/`: Markdown documentation
- `dist/html/`: static HTML site with local API and content search

## Configure the public build

The generated metadata uses `https://scrapmechanicdocs.com/` by default. Set `SM_DOCS_SITE_URL` when publishing at another URL:

```bash
SM_DOCS_SITE_URL="https://owner.github.io/repository/" \
uv run python main.py
```

`SM_DOCS_SITE_URL` is the full public base URL. It includes the scheme, hostname, and any deployment path, and is used for canonical URLs, social metadata, the sitemap, and 404-page links.

For GitHub Pages deployments, configure the custom domain in the repository's Pages settings. GitHub Actions deployments do not require or use a `CNAME` file. The deployment workflow passes the configured Pages URL to the generator automatically.

The build date is always the current UTC date. The published API files do not identify a target game version.

The HTML output also includes `404.html`, `.nojekyll`, `robots.txt`, and `sitemap.xml` for static hosting.

## Preview the HTML site

```bash
python -m http.server 8000 --directory dist/html
```

Open <http://localhost:8000/>.

## Run checks

Generate the site, then run:

```bash
uv run python -m unittest discover -s tests
node tests/search_quality.js
```
