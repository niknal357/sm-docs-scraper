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
    'hierarchy',
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

  const identifierKey = (value) => normalizeIdentifier(value).replace(/[^a-z0-9]+/g, '');

  const editDistance = (left, right) => {
    const rows = Array.from(
      { length: left.length + 1 },
      (_, row) => Array.from({ length: right.length + 1 }, (_, column) => (
        row === 0 ? column : column === 0 ? row : 0
      )),
    );
    for (let row = 1; row <= left.length; row += 1) {
      for (let column = 1; column <= right.length; column += 1) {
        const cost = left[row - 1] === right[column - 1] ? 0 : 1;
        rows[row][column] = Math.min(
          rows[row - 1][column] + 1,
          rows[row][column - 1] + 1,
          rows[row - 1][column - 1] + cost,
        );
        if (row > 1 && column > 1
            && left[row - 1] === right[column - 2]
            && left[row - 2] === right[column - 1]) {
          rows[row][column] = Math.min(rows[row][column], rows[row - 2][column - 2] + 1);
        }
      }
    }
    return rows[left.length][right.length];
  };

  const directFuzzyDistance = (queryKey, nameKey) => {
    if (queryKey.length < 4 || !nameKey) return null;
    const maximum = Math.max(1, Math.floor(queryKey.length * 0.25));
    if (Math.abs(queryKey.length - nameKey.length) > maximum) return null;
    const distance = editDistance(queryKey, nameKey);
    return distance <= maximum ? distance : null;
  };

  const matchRank = (record, query) => {
    const normalized = normalizeIdentifier(query);
    const qualified = normalizeIdentifier(record.qualifiedName);
    const name = normalizeIdentifier(record.name);
    const aliasValues = aliases(record);
    const normalizedAliases = aliasValues.map(normalizeIdentifier);
    const queryKey = identifierKey(query);
    const nameKey = identifierKey(record.name);
    const qualifiedKey = identifierKey(record.qualifiedName);
    const defaultRank = { completion: Number.MAX_SAFE_INTEGER, distance: Number.MAX_SAFE_INTEGER };

    if (qualified === normalized) return { ...defaultRank, tier: 0 };
    if (name === normalized) return { ...defaultRank, tier: 1 };
    if (normalizedAliases.includes(normalized)) return { ...defaultRank, tier: 2 };

    if (queryKey.length >= 3 && nameKey.startsWith(queryKey)) {
      return { ...defaultRank, tier: 3, completion: nameKey.length - queryKey.length };
    }
    const queryHasPath = /[._:]/.test(normalized);
    if (queryHasPath && queryKey.length >= 3 && qualifiedKey.startsWith(queryKey)) {
      return { ...defaultRank, tier: 3, completion: qualifiedKey.length - queryKey.length };
    }

    const distance = directFuzzyDistance(queryKey, nameKey);
    if (distance !== null) return { ...defaultRank, tier: 4, distance };

    const queryWords = identifierWords(query);
    const nameWords = identifierWords(record.name);
    if (queryWords.length === 1
        && nameWords.some((word) => word.startsWith(queryWords[0]))) {
      return {
        ...defaultRank,
        tier: 5,
        completion: nameKey.length - queryWords[0].length,
      };
    }
    if (everyWordMatches(queryWords, record.name)) return { ...defaultRank, tier: 5 };

    const identifierText = [record.qualifiedName, ...aliasValues].join(' ');
    if ((queryKey.length >= 3 && qualifiedKey.startsWith(queryKey))
        || everyWordMatches(queryWords, identifierText)) {
      return {
        ...defaultRank,
        tier: 6,
        completion: qualifiedKey.startsWith(queryKey)
          ? qualifiedKey.length - queryKey.length
          : defaultRank.completion,
      };
    }

    const prose = `${record.signature} ${record.summary} ${record.types}`;
    if (everyWordMatches(queryWords, prose)) return { ...defaultRank, tier: 7 };
    return { ...defaultRank, tier: 8 };
  };

  const matchTier = (record, query) => matchRank(record, query).tier;

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
      const rank = matchRank(record, query);
      const candidate = candidates.get(record.id);
      if (candidate) Object.assign(candidate, rank);
      else if (rank.tier <= 7) candidates.set(record.id, { ...record, ...rank, score: 0 });
    });

    const ranked = [...candidates.values()].map((record) => ({
      ...record,
      contextBoost: currentEnvironment !== 'All'
        && record.environment === currentEnvironment ? 0.1 : 0,
    })).filter((record) => environment === 'All' || record.environment === environment)
      .sort((left, right) => (
        left.tier - right.tier
        || left.distance - right.distance
        || left.completion - right.completion
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
