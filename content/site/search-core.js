(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.SmDocsSearch = factory();
  }
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  const SEARCH_FIELDS = [
    'qualifiedName',
    'name',
    'aliases',
    'parentPage',
    'signature',
    'summary',
    'types',
  ];
  const STORE_FIELDS = [
    ...SEARCH_FIELDS,
    'parameterTypes',
    'returnTypes',
    'environment',
    'kind',
    'pageKind',
    'availability',
    'url',
  ];

  const normalizeIdentifier = (value) => value
    .trim()
    .replace(/\s*\([^)]*\)\s*$/, '')
    .toLocaleLowerCase();

  const identifierWords = (value) => value
    .replace(/[._:]/g, ' ')
    .replace(/([a-z0-9])([A-Z])/g, '$1 $2')
    .toLocaleLowerCase()
    .trim()
    .split(/\s+/)
    .filter(Boolean);

  const wordSet = (value) => new Set(identifierWords(value));

  const everyWordMatches = (queryWords, value) => {
    const words = wordSet(value);
    return queryWords.length > 0 && queryWords.every((word) => words.has(word));
  };

  const aliases = (record) => record.aliases ? record.aliases.split('\n') : [];

  const matchTier = (record, query) => {
    const normalized = normalizeIdentifier(query);
    const qualified = normalizeIdentifier(record.qualifiedName);
    const name = normalizeIdentifier(record.name);
    const aliasValues = aliases(record);

    if (qualified === normalized) return 0;
    if (name === normalized) return 1;
    if (aliasValues.some((alias) => normalizeIdentifier(alias) === normalized)) return 2;

    if (normalized.length >= 3) {
      const identifiers = [record.qualifiedName, record.name, ...aliasValues];
      if (identifiers.some((value) => normalizeIdentifier(value).startsWith(normalized))) {
        return 3;
      }
    }

    const queryWords = identifierWords(query);
    const identifierText = [record.qualifiedName, record.name, ...aliasValues].join(' ');
    if (everyWordMatches(queryWords, identifierText)) return 3;

    const prose = `${record.signature} ${record.summary} ${record.types}`;
    if (everyWordMatches(queryWords, prose)) return 4;
    return 5;
  };

  const create = (records, MiniSearch) => {
    const engine = new MiniSearch({
      fields: SEARCH_FIELDS,
      storeFields: STORE_FIELDS,
      searchOptions: {
        boost: {
          qualifiedName: 12,
          name: 10,
          aliases: 8,
          parentPage: 4,
          signature: 3,
          summary: 1.5,
          types: 1,
        },
      },
    });
    engine.addAll(records);
    return { engine, records, recordsById: new Map(records.map((record) => [record.id, record])) };
  };

  const search = (state, query, options = {}) => {
    const environment = options.environment || 'All';
    const currentEnvironment = options.currentEnvironment || 'All';
    const miniResults = state.engine.search(query, {
      combineWith: 'AND',
      prefix: (term) => term.length >= 3,
      fuzzy: (term) => term.length >= 4 ? 0.25 : false,
    });
    const candidates = new Map();

    miniResults.forEach((result) => {
      const record = state.recordsById.get(result.id);
      if (record) candidates.set(result.id, { ...record, score: result.score });
    });

    state.records.forEach((record) => {
      const tier = matchTier(record, query);
      if (tier <= 4 && !candidates.has(record.id)) {
        candidates.set(record.id, { ...record, score: 0 });
      }
    });

    const ranked = [...candidates.values()].map((record) => ({
      ...record,
      tier: matchTier(record, query),
      contextBoost: currentEnvironment !== 'All'
        && record.environment === currentEnvironment ? 0.1 : 0,
    })).filter((record) => environment === 'All' || record.environment === environment)
      .sort((left, right) => (
        left.tier - right.tier
        || (right.score + right.contextBoost) - (left.score + left.contextBoost)
        || left.qualifiedName.localeCompare(right.qualifiedName)
      ));

    const groups = new Map();
    const results = [];
    ranked.forEach((record) => {
      const group = `${record.environment}\n${record.kind}\n${record.qualifiedName}`;
      const existing = groups.get(group);
      if (existing) {
        existing.overloadCount += 1;
        return;
      }
      record.overloadCount = 1;
      groups.set(group, record);
      results.push(record);
    });

    const suggestions = state.engine.autoSuggest(query, {
      combineWith: 'AND',
      fuzzy: (term) => term.length >= 4 ? 0.25 : false,
    }).slice(0, 3).map((item) => item.suggestion);

    return { results, suggestions };
  };

  return {
    create,
    identifierWords,
    matchTier,
    normalizeIdentifier,
    search,
  };
});
