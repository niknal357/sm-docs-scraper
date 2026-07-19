# Search TODO

## Goal

Replace the current sidebar page filter with fast, API-aware documentation search.

Search should support two common intents:

1. Looking up an API symbol such as `sm.physics.raycast`.
2. Finding documentation by description, such as `collision filter`.

## Preferred architecture

Use two local indexes behind one search interface.

### API symbol index

Use [MiniSearch](https://github.com/lucaong/minisearch) with records generated directly from the documentation IR.

Create one record for each:

- Page
- Function or operation
- Constant
- Member
- Callback

Store these fields where available:

- Qualified name
- Short name
- Search aliases
- Parent page
- Signature
- Summary
- Parameter and return types
- Environment
- Symbol kind
- Availability
- Direct anchor URL

MiniSearch provides exact, prefix, fuzzy, field-boosted, and suggestion searches without a server.

### Documentation content index

Use [Pagefind](https://pagefind.app/) to index descriptions, examples, parameters, and other rendered content.

Pagefind provides:

- Static search without hosted infrastructure
- Low-bandwidth index loading
- Heading-level results and direct links
- Highlighted excerpts
- Compound identifier handling
- A Python wrapper that fits the current build

Only index the main documentation content. Exclude navigation, breadcrumbs, and the table of contents.

### Combined interface

Search both indexes and group results into:

- **API symbols**
- **Documentation**

Show the following for symbol results:

- Qualified name
- Symbol kind
- Environment
- Signature
- Short description

Show the page hierarchy, matching heading, and excerpt for documentation results.

## Implementation plan

### 1. Prepare stable links

- [x] Ensure every searchable page and symbol has a stable anchor.
- [x] Remove duplicate HTML IDs.
- [x] Decide whether overloads share one result or have unique anchors.
- [x] Keep callback aliases such as `onCreate`, `server_onCreate`, and `client_onCreate` searchable.
- [x] Add tests that verify every indexed URL points to generated HTML.

### 2. Generate the symbol index

- [x] Add a search-record model to the renderer.
- [x] Generate records from the IR instead of parsing rendered HTML.
- [x] Create qualified names using the correct namespace or userdata syntax.
- [x] Add normalized aliases for dotted, colon-separated, snake-case, and camel-case identifiers.
- [x] Include common variants such as `raycast` and `ray cast`.
- [x] Group duplicate overloads when appropriate.
- [x] Serialize the records or MiniSearch index into `dist/html/assets/`.
- [x] Load the symbol index when search is first opened or focused.

### 3. Add Pagefind

- [x] Add the Pagefind Python package to the build dependencies.
- [x] Mark the main documentation element with `data-pagefind-body`.
- [x] Run Pagefind after HTML generation.
- [x] Preserve useful identifier characters such as `.`, `_`, and `:`.
- [x] Enable heading-level sub-results.
- [x] Confirm nested pages and deployments under a URL subpath work.
- [x] Verify that sidebar content is absent from the search index.

### 4. Build the search interface

- [x] Replace the current sidebar filtering behavior with a search panel or modal.
- [x] Search both indexes from the same input.
- [x] Group symbol and documentation results clearly.
- [x] Highlight matching terms.
- [x] Limit the initial result count and provide a way to see more.
- [x] Add `All`, `Game`, and `Terrain` filters.
- [ ] Consider filters for functions, types, callbacks, and constants.
- [x] Soft-boost results from the current environment without hiding other results.
- [x] Add a copy-signature action to exact symbol matches.
- [x] Use a compact search popover with a separate all-results page.

### 5. Keyboard and accessibility

- [x] Add `Ctrl/Cmd+K` and `/` shortcuts.
- [x] Support arrow-key result navigation.
- [x] Open the selected result with Enter.
- [x] Close or clear search with Escape.
- [x] Use the ARIA combobox and listbox patterns.
- [x] Give the input an accessible name.
- [x] Announce result counts and loading state.
- [x] Keep focus behavior predictable when the popover closes.

### 6. Ranking

Rank matches in this general order:

1. Exact qualified identifier
2. Exact short symbol name
3. Identifier prefix
4. Camel-case, underscore, colon, or dot-separated token match
5. All query words in the signature or summary
6. Fuzzy symbol match
7. General documentation text match

Additional rules:

- [x] Keep exact identifier matching separate from stemmed prose matching.
- [x] Require stronger matches for short terms such as `sm`, `id`, and `ui`.
- [x] Apply fuzzy matching mainly to terms of four or more characters.
- [x] Prevent popularity or context boosts from outranking a strong exact match.

### 7. Empty and initial states

- [x] Show recent symbols when search opens with no query.
- [ ] Optionally let users pin frequent symbols in local storage.
- [x] Show spelling suggestions when no exact results exist.
- [x] Show related, less strict results instead of an empty panel.
- [ ] Add a link for reporting a missing result.
- [x] Restore sidebar expansion state after search; search must not modify it.

### 8. Search quality tests

Create a checked-in set of representative queries and expected results.

Initial cases:

| Query | Expected result |
| --- | --- |
| `raycast` | `sm.physics.raycast` |
| `ray cast` | `sm.physics.raycast` |
| `sm.physics.raycast` | Exact function result |
| `raycats` | Suggest `raycast` |
| `collision filter` | `sm.physics.filter` |
| `server on create` | Class `onCreate` callbacks |
| `create joint` | `Shape:createJoint` |
| `get raycast` | `sm.localPlayer.getRaycast` |

- [x] Assert that expected results remain within the top three.
- [x] Test Game and Terrain duplicates.
- [x] Test overload grouping.
- [x] Test direct anchors.
- [x] Test keyboard navigation and mobile behavior.
- [x] Record index size and first-search latency.

### 9. Feedback and analytics

Only add analytics if it can be done with acceptable privacy controls.

Useful signals are:

- Popular queries
- Queries with no results
- Selected result and its position
- Queries that are immediately rewritten

Use these signals to improve aliases, ranking, and missing documentation.

## Alternatives

### Algolia DocSearch

Consider Algolia DocSearch if a hosted service is acceptable. It includes hierarchical indexing, typo tolerance, snippets, facets, contextual search, analytics, recent searches, and optional grounded AI answers.

Trade-offs include an external dependency, crawler configuration, and less control over offline use.

### AI answers

Treat AI answers as a later, separate **Ask** mode. Keep normal symbol search as the default, and require AI answers to include links or citations to the source documentation.

## References

- [How GitHub Docs' search works](https://github.blog/engineering/architecture-optimization/how-github-docs-new-search-works/)
- [Pagefind](https://pagefind.app/)
- [Pagefind sub-results](https://pagefind.app/docs/sub-results/)
- [Pagefind indexing controls](https://pagefind.app/docs/indexing/)
- [Pagefind Python API](https://pagefind.app/docs/py-api/)
- [MiniSearch](https://github.com/lucaong/minisearch)
- [Algolia DocSearch configuration](https://docsearch.algolia.com/docs/required-configuration)
- [Docusaurus contextual search](https://docusaurus.io/docs/search#contextual-search)
- [Algolia search analytics](https://algolia.com/doc/guides/search-analytics/overview)
- [Elasticsearch ranking evaluation](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/search-rank-eval)
