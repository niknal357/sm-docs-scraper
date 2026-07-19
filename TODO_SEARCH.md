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

- [ ] Ensure every searchable page and symbol has a stable anchor.
- [ ] Remove duplicate HTML IDs.
- [ ] Decide whether overloads share one result or have unique anchors.
- [ ] Keep callback aliases such as `onCreate`, `server_onCreate`, and `client_onCreate` searchable.
- [ ] Add tests that verify every indexed URL points to generated HTML.

### 2. Generate the symbol index

- [ ] Add a search-record model to the renderer.
- [ ] Generate records from the IR instead of parsing rendered HTML.
- [ ] Create qualified names using the correct namespace or userdata syntax.
- [ ] Add normalized aliases for dotted, colon-separated, snake-case, and camel-case identifiers.
- [ ] Include common variants such as `raycast` and `ray cast`.
- [ ] Group duplicate overloads when appropriate.
- [ ] Serialize the records or MiniSearch index into `dist/html/assets/`.
- [ ] Load the symbol index when search is first opened or focused.

### 3. Add Pagefind

- [ ] Add the Pagefind Python package to the build dependencies.
- [ ] Mark the main documentation element with `data-pagefind-body`.
- [ ] Run Pagefind after HTML generation.
- [ ] Preserve useful identifier characters such as `.`, `_`, and `:`.
- [ ] Enable heading-level sub-results.
- [ ] Confirm nested pages and deployments under a URL subpath work.
- [ ] Verify that sidebar content is absent from the search index.

### 4. Build the search interface

- [ ] Replace the current sidebar filtering behavior with a search panel or modal.
- [ ] Search both indexes from the same input.
- [ ] Group symbol and documentation results clearly.
- [ ] Highlight matching terms.
- [ ] Limit the initial result count and provide a way to see more.
- [ ] Add `All`, `Game`, and `Terrain` filters.
- [ ] Consider filters for functions, types, callbacks, and constants.
- [ ] Soft-boost results from the current environment without hiding other results.
- [ ] Add a copy-signature action to exact symbol matches.
- [ ] Use a full-width search dialog on small screens.

### 5. Keyboard and accessibility

- [ ] Add `Ctrl/Cmd+K` and `/` shortcuts.
- [ ] Support arrow-key result navigation.
- [ ] Open the selected result with Enter.
- [ ] Close or clear search with Escape.
- [ ] Use the ARIA combobox and listbox patterns.
- [ ] Give the input an accessible name.
- [ ] Announce result counts and loading state.
- [ ] Restore focus when the modal closes.

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

- [ ] Keep exact identifier matching separate from stemmed prose matching.
- [ ] Require stronger matches for short terms such as `sm`, `id`, and `ui`.
- [ ] Apply fuzzy matching mainly to terms of four or more characters.
- [ ] Prevent popularity or context boosts from outranking a strong exact match.

### 7. Empty and initial states

- [ ] Show recent symbols when search opens with no query.
- [ ] Optionally let users pin frequent symbols in local storage.
- [ ] Show spelling suggestions when no exact results exist.
- [ ] Show related, less strict results instead of an empty panel.
- [ ] Add a link for reporting a missing result.
- [ ] Restore sidebar expansion state after search; search must not modify it.

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

- [ ] Assert that expected results remain within the top three.
- [ ] Test Game and Terrain duplicates.
- [ ] Test overload grouping.
- [ ] Test direct anchors.
- [ ] Test keyboard navigation and mobile behavior.
- [ ] Record index size and first-search latency.

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
