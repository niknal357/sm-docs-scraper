'use strict';

const fs = require('fs');
const path = require('path');
const MiniSearch = require('../content/site/vendor/minisearch.js');
const Search = require('../content/site/search-core.js');

const indexPath = process.argv[2] || path.join('dist', 'html', 'assets', 'search-symbols.json');
const cases = JSON.parse(fs.readFileSync(path.join(__dirname, 'search_quality.json'), 'utf8'));
const payload = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
const started = performance.now();
const state = Search.create(payload.records, MiniSearch);
const buildTime = performance.now() - started;
const failures = [];

for (const testCase of cases) {
  const output = Search.search(state, testCase.query, {
    environment: 'All',
    currentEnvironment: 'Game',
  });
  const rank = output.results.findIndex((record) => (
    (!testCase.qualifiedName || record.qualifiedName === testCase.qualifiedName)
    && (!testCase.name || record.name === testCase.name)
    && (!testCase.kind || record.kind === testCase.kind)
  )) + 1;

  if (rank === 0 || rank > testCase.maxRank) {
    failures.push(
      `${JSON.stringify(testCase.query)}: expected result within rank ${testCase.maxRank}, got ${rank || 'no match'}`
    );
  }
  if (testCase.expectedSuggestion
      && !output.suggestions.includes(testCase.expectedSuggestion)) {
    failures.push(
      `${JSON.stringify(testCase.query)}: missing suggestion ${JSON.stringify(testCase.expectedSuggestion)}`
    );
  }
}

const duplicateQuery = (environment) => Search.search(state, 'sm.color.new', {
  environment,
  currentEnvironment: 'Game',
}).results;
const allDuplicates = duplicateQuery('All').filter(
  (record) => record.qualifiedName === 'sm.color.new'
);
if (allDuplicates.length !== 2 || allDuplicates.some((record) => record.overloadCount !== 4)) {
  failures.push('sm.color.new: expected four overloads grouped once per environment');
}
if (duplicateQuery('Terrain').some((record) => record.environment !== 'Terrain')) {
  failures.push('Terrain filter returned a result from another environment');
}

if (failures.length) {
  console.error(failures.join('\n'));
  process.exit(1);
}

console.log(
  `Search quality passed: ${cases.length} queries, ${payload.records.length} records, index built in ${buildTime.toFixed(1)}ms.`
);
