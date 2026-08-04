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
- `dist/html/`: deployable static site with HTML, Markdown, symbol pages, and local search

## Configure the public build

The generated metadata uses `https://scrapmechanicdocs.com/` by default. Set `SM_DOCS_SITE_URL` when publishing at another URL:

```bash
SM_DOCS_SITE_URL="https://owner.github.io/repository/" \
uv run python main.py
```

`SM_DOCS_SITE_URL` is the full public base URL. It includes the scheme, hostname, and any deployment path, and is used for canonical URLs, social metadata, the sitemap, and 404-page links.

For GitHub Pages deployments, configure the custom domain in the repository's Pages settings. GitHub Actions deployments do not require or use a `CNAME` file. The deployment workflow passes the configured Pages URL to the generator automatically.

The build date is always the current UTC date. The published API files do not identify a target game version.

The Pages workflow periodically checks the official JSON documentation. Scheduled runs deploy only when its extracted contents differ from the last successful deployment. Pushes and manual runs always deploy. A failed check or build leaves the existing site online.

The deployed output also includes `llms.txt`, focused HTML and Markdown symbol pages, `page-digests.json`, `404.html`, `.nojekyll`, `robots.txt`, `sitemap.xml`, and the API source digest.

Sitemap modification dates are retained when a page's generated Markdown has not changed. The Pages workflow reads the digest data from the previous deployment before each build.

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
