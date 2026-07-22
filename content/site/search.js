(() => {
  'use strict';

  const searchRoot = document.getElementById('navbar-search');
  if (!searchRoot) return;

  const input = document.getElementById('site-search-input');
  const popover = document.getElementById('search-popover');
  const popoverResults = document.getElementById('search-popover-results');
  const popoverStatus = document.getElementById('search-popover-status');
  const seeAll = document.getElementById('search-see-all');
  const searchPage = document.querySelector('[data-search-page]');
  const searchPageResults = document.getElementById('search-page-results');
  const searchPageStatus = document.getElementById('search-page-status');
  const pageFilterButtons = searchPage
    ? [...searchPage.querySelectorAll('[data-search-environment]')]
    : [];
  const currentEnvironment = searchRoot.dataset.currentEnvironment || 'All';
  const siteHome = new URL(searchRoot.dataset.siteHome, window.location.href);
  const siteRoot = new URL('.', siteHome);
  const recentKey = 'sm-docs-recent-symbols';
  const recentLimit = 4;
  const popupLimit = 6;
  const pageStep = 20;

  let selectedIndex = -1;
  let optionSequence = 0;
  let popupVersion = 0;
  let pageVersion = 0;
  let pageEnvironment = 'All';
  let pageLimit = pageStep;
  let inputTimer;
  let symbolStatePromise;
  let pagefindPromise;

  const resolveAsset = (path) => new URL(path, window.location.href).href;
  const resolveSymbolUrl = (path) => new URL(path.replace(/^\/+/, ''), siteRoot).href;
  const resolvePagefindUrl = (path) => new URL(path, window.location.origin).href;
  const canonicalResultUrl = (path) => {
    const url = new URL(path);
    url.hash = '';
    url.search = '';
    return url.href.replace(/\/index\.html$/, '/');
  };

  const loadSymbolState = () => {
    if (!symbolStatePromise) {
      symbolStatePromise = fetch(resolveAsset(searchRoot.dataset.symbolIndex))
        .then((response) => {
          if (!response.ok) throw new Error(`Symbol index returned ${response.status}`);
          return response.json();
        })
        .then((payload) => {
          if (payload.version !== 1 || !Array.isArray(payload.records)) {
            throw new Error('Unsupported symbol index');
          }
          return window.SmDocsSearch.create(payload.records, window.MiniSearch);
        });
    }
    return symbolStatePromise;
  };

  const loadPagefind = () => {
    if (!pagefindPromise) {
      pagefindPromise = import(resolveAsset(searchRoot.dataset.pagefindModule))
        .then(async (pagefind) => {
          await pagefind.options({
            baseUrl: siteRoot.pathname,
            excerptLength: 24,
          });
          return pagefind;
        });
    }
    return pagefindPromise;
  };

  const readRecentIds = () => {
    try {
      const value = JSON.parse(localStorage.getItem(recentKey) || '[]');
      return Array.isArray(value) ? value.filter((item) => typeof item === 'string') : [];
    } catch (_) {
      return [];
    }
  };

  const rememberSymbol = (id) => {
    const values = [id, ...readRecentIds().filter((value) => value !== id)].slice(0, 8);
    try {
      localStorage.setItem(recentKey, JSON.stringify(values));
    } catch (_) {}
  };

  const appendHierarchy = (element, value) => {
    if (!value) return;
    const hierarchy = document.createElement('div');
    hierarchy.className = 'search-result-hierarchy';
    hierarchy.textContent = value;
    element.append(hierarchy);
  };

  const appendHighlighted = (element, text, query) => {
    if (!text) return;
    const terms = [...new Set(window.SmDocsSearch.identifierWords(query))]
      .filter((term) => term.length >= 2)
      .sort((left, right) => right.length - left.length);
    if (!terms.length) {
      element.textContent = text;
      return;
    }

    const escaped = terms.map((term) => term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
    const pattern = new RegExp(`(${escaped.join('|')})`, 'gi');
    text.split(pattern).forEach((part) => {
      if (terms.some((term) => term.toLocaleLowerCase() === part.toLocaleLowerCase())) {
        const mark = document.createElement('mark');
        mark.textContent = part;
        element.append(mark);
      } else {
        element.append(document.createTextNode(part));
      }
    });
  };

  const appendSafeExcerpt = (element, excerpt) => {
    const parsed = new DOMParser().parseFromString(excerpt || '', 'text/html');
    const append = (node, parent) => {
      if (node.nodeType === Node.TEXT_NODE) {
        parent.append(document.createTextNode(node.textContent));
        return;
      }
      if (node.nodeType !== Node.ELEMENT_NODE) return;
      const target = node.tagName === 'MARK' ? document.createElement('mark') : parent;
      if (target !== parent) parent.append(target);
      node.childNodes.forEach((child) => append(child, target));
    };
    parsed.body.childNodes.forEach((node) => append(node, element));
  };

  const popupOptions = () => [...popoverResults.querySelectorAll('[role="option"]')];

  const selectOption = (optionOrIndex) => {
    const options = popupOptions();
    if (!options.length) {
      selectedIndex = -1;
      input.removeAttribute('aria-activedescendant');
      return;
    }
    const index = typeof optionOrIndex === 'number'
      ? (optionOrIndex + options.length) % options.length
      : options.indexOf(optionOrIndex);
    selectedIndex = index;
    options.forEach((option, optionIndex) => {
      option.setAttribute('aria-selected', String(optionIndex === index));
    });
    const selected = options[index];
    input.setAttribute('aria-activedescendant', selected.id);
    selected.scrollIntoView({ block: 'nearest' });
  };

  const resetSelection = () => {
    selectedIndex = -1;
    input.removeAttribute('aria-activedescendant');
  };

  const createResultLink = (href, popupOption, onSelect) => {
    const link = document.createElement('a');
    link.className = 'search-result-link';
    link.href = href;
    if (popupOption) {
      link.id = `search-option-${optionSequence}`;
      optionSequence += 1;
      link.setAttribute('role', 'option');
      link.setAttribute('aria-selected', 'false');
      link.addEventListener('mouseenter', () => selectOption(link));
      link.addEventListener('click', () => closePopover());
    }
    if (onSelect) link.addEventListener('click', onSelect);
    return link;
  };

  const createSymbolResult = (record, query, options = {}) => {
    const row = document.createElement('div');
    row.className = `search-result${options.compact ? ' compact' : ''}`;
    const link = createResultLink(
      resolveSymbolUrl(record.url),
      options.popupOption,
      () => rememberSymbol(record.id),
    );

    if (options.compact) {
      const primary = document.createElement(record.signature ? 'code' : 'strong');
      primary.className = record.signature
        ? 'search-result-primary search-result-signature'
        : 'search-result-primary';
      appendHighlighted(
        primary,
        record.signature ? record.signature.split('\n')[0] : record.qualifiedName,
        query,
      );
      link.append(primary);

      appendHierarchy(link, record.hierarchy);
    } else {
      const heading = document.createElement('div');
      heading.className = 'search-result-heading';
      const name = document.createElement('strong');
      appendHighlighted(name, record.qualifiedName, query);
      heading.append(name);
      link.append(heading);
      appendHierarchy(link, record.hierarchy);

      if (record.signature) {
        const signature = document.createElement('code');
        signature.className = 'search-result-signature';
        signature.textContent = record.signature.split('\n')[0];
        link.append(signature);
      }
      if (record.summary) {
        const summary = document.createElement('p');
        appendHighlighted(summary, record.summary, query);
        link.append(summary);
      }

    }
    row.append(link);

    if (!options.compact && record.signature && navigator.clipboard) {
      const copy = document.createElement('button');
      copy.className = 'search-copy';
      copy.type = 'button';
      copy.textContent = 'Copy signature';
      copy.setAttribute('aria-label', `Copy signature for ${record.qualifiedName}`);
      copy.addEventListener('click', async () => {
        await navigator.clipboard.writeText(record.signature);
        if (searchPageStatus) {
          searchPageStatus.textContent = `Copied the signature for ${record.qualifiedName}.`;
        }
      });
      row.append(copy);
    }
    return row;
  };

  const createDocumentationResult = (record, options = {}) => {
    const row = document.createElement('div');
    row.className = `search-result documentation-result${options.compact ? ' compact' : ''}`;
    const link = createResultLink(resolvePagefindUrl(record.url), options.popupOption);
    const heading = document.createElement('div');
    heading.className = 'search-result-heading';
    const title = document.createElement('strong');
    title.textContent = record.title;
    heading.append(title);
    link.append(heading);

    if (record.hierarchy && record.hierarchy !== record.title) {
      appendHierarchy(link, record.hierarchy);
    }
    if (record.excerpt) {
      const excerpt = document.createElement('p');
      appendSafeExcerpt(excerpt, record.excerpt);
      link.append(excerpt);
    }
    row.append(link);
    return row;
  };

  const createSection = (title, count, compact) => {
    const section = document.createElement('section');
    section.className = `search-result-section${compact ? ' compact' : ''}`;
    section.setAttribute('aria-label', title);
    const heading = document.createElement(compact ? 'h3' : 'h2');
    heading.textContent = compact ? title : `${title} (${count})`;
    section.append(heading);
    return section;
  };

  const documentationSearch = async (query, environment, maximum, symbolResults) => {
    const pagefind = await loadPagefind();
    const searchOptions = environment === 'All' ? {} : { filters: { environment } };
    const search = await pagefind.search(query, searchOptions);
    const requested = Math.max(maximum * 2, 12);
    const selected = search.results.slice(0, requested);
    const loaded = await Promise.all(selected.map(async (result) => ({
      data: await result.data(),
      score: result.score,
    })));
    const strongestScore = selected.length ? selected[0].score : 0;
    const symbolUrls = new Set(symbolResults.map((record) => (
      canonicalResultUrl(resolveSymbolUrl(record.url))
    )));
    const queryKey = query.toLocaleLowerCase().replace(/[^a-z0-9]+/g, '');
    const records = loaded.map(({ data, score }) => {
      const result = data.sub_results && data.sub_results.length
        ? data.sub_results[0]
        : data;
      return {
        title: result.title || data.meta.title || 'Documentation',
        url: result.url || data.url,
        excerpt: result.excerpt || data.excerpt,
        hierarchy: data.meta.hierarchy || data.meta.title || '',
        score,
      };
    }).filter((record) => {
      const url = canonicalResultUrl(resolvePagefindUrl(record.url));
      if (symbolUrls.has(url) || record.score < strongestScore * 0.1) return false;
      const titleKey = record.title.toLocaleLowerCase().replace(/[^a-z0-9]+/g, '');
      const titleMatches = queryKey.length >= 3
        && (titleKey.startsWith(queryKey) || titleKey.includes(queryKey));
      const markIndex = (record.excerpt || '').search(/<mark(?:\s|>)/i);
      const wordsBeforeMatch = markIndex < 0
        ? Number.MAX_SAFE_INTEGER
        : record.excerpt.slice(0, markIndex).replace(/<[^>]*>/g, ' ').trim().split(/\s+/)
          .filter(Boolean).length;
      return titleMatches || wordsBeforeMatch <= 8;
    }).map(({ score: _, ...record }) => record);
    return {
      records,
      total: records.length,
      hasMore: search.results.length > selected.length,
    };
  };

  const combinedSearch = async (query, environment, documentationLimit) => {
    const state = await loadSymbolState();
    const symbols = window.SmDocsSearch.search(state, query, {
      environment,
      currentEnvironment,
    });
    let documentation;
    try {
      documentation = await documentationSearch(
        query,
        environment,
        documentationLimit,
        symbols.results,
      );
    } catch (error) {
      console.error('Documentation search failed', error);
      documentation = { records: [], total: 0, hasMore: false };
    }
    return { symbols, documentation };
  };

  const searchPageUrl = (query, environment = 'All') => {
    const url = new URL('search.html', siteRoot);
    if (query) url.searchParams.set('q', query);
    if (environment !== 'All') url.searchParams.set('environment', environment);
    return url;
  };

  const openPopover = () => {
    popover.hidden = false;
    input.setAttribute('aria-expanded', 'true');
  };

  const closePopover = () => {
    popover.hidden = true;
    input.setAttribute('aria-expanded', 'false');
    popupVersion += 1;
    resetSelection();
  };

  const setPopupBusy = (busy, status) => {
    popover.setAttribute('aria-busy', String(busy));
    popoverStatus.textContent = status;
  };

  const renderPopupInitial = async () => {
    const version = ++popupVersion;
    openPopover();
    setPopupBusy(true, 'Loading recent symbols…');
    try {
      const state = await loadSymbolState();
      if (version !== popupVersion) return;
      const recent = readRecentIds().map((id) => state.recordsById.get(id)).filter(Boolean)
        .slice(0, recentLimit);
      popoverResults.replaceChildren();
      optionSequence = 0;
      resetSelection();
      if (recent.length) {
        const section = createSection('Recent', recent.length, true);
        recent.forEach((record) => section.append(createSymbolResult(record, '', {
          compact: true,
          popupOption: true,
        })));
        popoverResults.append(section);
        popoverStatus.textContent = `${recent.length} recent symbol${recent.length === 1 ? '' : 's'}`;
      } else {
        const empty = document.createElement('p');
        empty.className = 'search-empty';
        empty.textContent = 'Start typing to search.';
        popoverResults.append(empty);
        popoverStatus.textContent = 'Ready to search';
      }
      seeAll.hidden = true;
      popover.setAttribute('aria-busy', 'false');
    } catch (error) {
      if (version === popupVersion) showPopupError(error);
    }
  };

  const mergeSearchResults = (output) => {
    const symbols = output.symbols.results;
    const documentation = output.documentation.records;
    const documentationFirst = !symbols.length || symbols[0].tier >= 7;
    const symbolWeight = documentationFirst ? 0.65 : 1;
    const documentationWeight = documentationFirst ? 1 : 0.4;
    return [
      ...symbols.map((record, index) => ({
        record,
        source: 'symbol',
        relevance: symbolWeight / (index + 1),
      })),
      ...documentation.map((record, index) => ({
        record,
        source: 'documentation',
        relevance: documentationWeight / (index + 1),
      })),
    ].sort((left, right) => {
      const relevanceDifference = right.relevance - left.relevance;
      if (relevanceDifference) return relevanceDifference;
      if (left.source === right.source) return 0;
      return left.source === 'documentation' ? -1 : 1;
    });
  };

  const renderPopupResults = (query, output) => {
    popoverResults.replaceChildren();
    optionSequence = 0;
    resetSelection();
    const results = mergeSearchResults(output).slice(0, popupLimit);

    if (results.length) {
      const section = document.createElement('section');
      section.setAttribute('aria-label', 'Search results');
      results.forEach(({ record, source }) => section.append(
        source === 'symbol'
          ? createSymbolResult(record, query, { compact: true, popupOption: true })
          : createDocumentationResult(record, { compact: true, popupOption: true })
      ));
      popoverResults.append(section);
    } else {
      const empty = document.createElement('p');
      empty.className = 'search-empty';
      empty.textContent = `No results for “${query}”.`;
      popoverResults.append(empty);
    }

    const total = output.symbols.results.length + output.documentation.total;
    const totalLabel = `${total}${output.documentation.hasMore ? '+' : ''}`;
    popoverStatus.textContent = `${totalLabel} result${total === 1 ? '' : 's'}`;
    seeAll.href = searchPageUrl(query, searchPage ? pageEnvironment : 'All').href;
    seeAll.textContent = `See all results${total ? ` (${totalLabel})` : ''}`;
    seeAll.hidden = false;
    popover.setAttribute('aria-busy', 'false');
  };

  const showPopupError = (error) => {
    console.error(error);
    popoverResults.replaceChildren();
    const message = document.createElement('p');
    message.className = 'search-empty';
    message.textContent = window.location.protocol === 'file:'
      ? 'Search requires the site to be served over HTTP.'
      : 'Search could not be loaded.';
    popoverResults.append(message);
    setPopupBusy(false, 'Search unavailable');
    seeAll.hidden = true;
  };

  const runPopupSearch = async () => {
    const query = input.value.trim();
    if (!query) {
      renderPopupInitial();
      return;
    }

    const version = ++popupVersion;
    openPopover();
    setPopupBusy(true, 'Searching…');
    seeAll.href = searchPageUrl(query, searchPage ? pageEnvironment : 'All').href;
    try {
      const output = await combinedSearch(
        query,
        searchPage ? pageEnvironment : 'All',
        popupLimit,
      );
      if (version !== popupVersion) return;
      renderPopupResults(query, output);
    } catch (error) {
      if (version === popupVersion) showPopupError(error);
    }
  };

  const renderPageResults = (query, output) => {
    searchPageResults.replaceChildren();
    const symbols = output.symbols.results;
    const results = mergeSearchResults(output);

    if (results.length) {
      const section = document.createElement('section');
      section.setAttribute('aria-label', 'Search results');
      results.slice(0, pageLimit).forEach(({ record, source }) => {
        section.append(source === 'symbol'
          ? createSymbolResult(record, query)
          : createDocumentationResult(record));
      });
      searchPageResults.append(section);
    } else {
      const empty = document.createElement('p');
      empty.className = 'search-empty';
      empty.textContent = `No results for “${query}”.`;
      searchPageResults.append(empty);
    }

    const suggestions = output.symbols.suggestions;
    if (suggestions.length && (!symbols.length || symbols[0].tier >= 5)) {
      const suggestionsElement = document.createElement('div');
      suggestionsElement.className = 'search-suggestions';
      suggestionsElement.append(document.createTextNode('Try: '));
      suggestions.forEach((suggestion) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.textContent = suggestion;
        button.addEventListener('click', () => {
          input.value = suggestion;
          pageLimit = pageStep;
          updatePageUrl();
          runPageSearch();
        });
        suggestionsElement.append(button);
      });
      searchPageResults.append(suggestionsElement);
    }

    if (results.length > pageLimit || output.documentation.hasMore) {
      const more = document.createElement('button');
      more.className = 'search-more';
      more.type = 'button';
      more.textContent = 'Show more results';
      more.addEventListener('click', () => {
        pageLimit += pageStep;
        runPageSearch();
      });
      searchPageResults.append(more);
    }

    const total = symbols.length + output.documentation.total;
    const totalLabel = `${total}${output.documentation.hasMore ? '+' : ''}`;
    searchPageStatus.textContent = `${totalLabel} result${total === 1 ? '' : 's'} found.`;
    searchPage.setAttribute('aria-busy', 'false');
  };

  const updatePageUrl = () => {
    if (!searchPage) return;
    const url = searchPageUrl(input.value.trim(), pageEnvironment);
    window.history.replaceState(null, '', url);
  };

  const runPageSearch = async () => {
    if (!searchPage) return;
    const query = input.value.trim();
    if (!query) {
      pageVersion += 1;
      searchPageResults.replaceChildren();
      searchPageStatus.textContent = 'Enter a query in the search bar.';
      updatePageUrl();
      return;
    }

    const version = ++pageVersion;
    searchPage.setAttribute('aria-busy', 'true');
    searchPageStatus.textContent = 'Searching…';
    try {
      const output = await combinedSearch(query, pageEnvironment, pageLimit);
      if (version !== pageVersion) return;
      renderPageResults(query, output);
      updatePageUrl();
    } catch (error) {
      if (version !== pageVersion) return;
      console.error(error);
      searchPageResults.replaceChildren();
      searchPageStatus.textContent = 'Search could not be loaded.';
      searchPage.setAttribute('aria-busy', 'false');
    }
  };

  const schedulePopupSearch = () => {
    clearTimeout(inputTimer);
    inputTimer = setTimeout(runPopupSearch, 140);
  };

  input.addEventListener('focus', () => {
    if (input.value.trim()) runPopupSearch();
    else renderPopupInitial();
  });
  input.addEventListener('input', schedulePopupSearch);
  input.addEventListener('keydown', (event) => {
    const options = popupOptions();
    if (event.key === 'ArrowDown' && options.length) {
      event.preventDefault();
      selectOption(selectedIndex + 1);
    } else if (event.key === 'ArrowUp' && options.length) {
      event.preventDefault();
      selectOption(selectedIndex < 0 ? options.length - 1 : selectedIndex - 1);
    } else if (event.key === 'Enter') {
      event.preventDefault();
      if (options.length) options[selectedIndex < 0 ? 0 : selectedIndex].click();
      else if (input.value.trim()) window.location.href = seeAll.href;
    } else if (event.key === 'Escape') {
      event.preventDefault();
      closePopover();
      input.blur();
    }
  });

  document.addEventListener('pointerdown', (event) => {
    if (!searchRoot.contains(event.target)) closePopover();
  });

  document.addEventListener('keydown', (event) => {
    const target = event.target;
    const editable = target instanceof HTMLElement
      && (target.matches('input, textarea, select') || target.isContentEditable);
    const command = (event.ctrlKey || event.metaKey)
      && !event.altKey
      && event.key.toLocaleLowerCase() === 'k';
    const slash = event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey;
    if (command || (slash && !editable)) {
      event.preventDefault();
      document.dispatchEvent(new CustomEvent('sm-docs:open-mobile-search'));
      input.focus({ preventScroll: true });
      input.select();
    }
  });

  if (/Mac|iPhone|iPad/.test(navigator.platform)) {
    const shortcut = searchRoot.querySelector('kbd');
    if (shortcut) shortcut.textContent = '⌘ K';
  }

  if (searchPage) {
    const parameters = new URLSearchParams(window.location.search);
    const requestedEnvironment = parameters.get('environment');
    if (['Game', 'Terrain'].includes(requestedEnvironment)) {
      pageEnvironment = requestedEnvironment;
    }
    input.value = parameters.get('q') || '';
    pageFilterButtons.forEach((button) => {
      button.setAttribute(
        'aria-pressed',
        String(button.dataset.searchEnvironment === pageEnvironment),
      );
      button.addEventListener('click', () => {
        pageEnvironment = button.dataset.searchEnvironment;
        pageFilterButtons.forEach((item) => {
          item.setAttribute('aria-pressed', String(item === button));
        });
        pageLimit = pageStep;
        updatePageUrl();
        runPageSearch();
      });
    });
    if (input.value.trim()) runPageSearch();
  }
})();
