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

## Preview the HTML site

```bash
python -m http.server 8000 --directory dist/html
```

Open <http://localhost:8000/>.

## Check search quality

Generate the site, then run:

```bash
node tests/search_quality.js
```
