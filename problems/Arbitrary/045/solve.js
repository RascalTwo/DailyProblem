const Tuple = (...args) => JSON.stringify(args);

/**
 * @param {number[][]} matrix
 * @param {Set<string>} seen
 * @param {number} r
 * @param {number} c
 * @returns {Set<string>}
 */
function collectIsland(matrix, seen, r, c) {
  seen.add(Tuple(r, c));

  for (const [ro, co] of [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ]) {
    const [nr, nc] = [r + ro, c + co];

    if (seen.has(Tuple(nr, nc))) continue;
    if (nr < 0 || nr >= matrix.length || nc < 0 || nc >= matrix[nr].length) continue;
    if (matrix[nr][nc] !== 1) continue;

    collectIsland(matrix, seen, nr, nc);
  }

  return seen;
}

/**
 * @param {number[][]} matrix
 * @param {number} r
 * @param {number} c
 * @returns {boolean}
 */
function isEdge(matrix, r, c) {
  return r === 0 || r === matrix.length - 1 || c === 0 || c === matrix[r].length - 1;
}

/**
 * @param {number[][]} matrix
 * @returns {number[][]}
 */
function removeIslands(matrix) {
  const processed = new Set();

  for (const [r, row] of matrix.entries()) {
    for (const [c, col] of row.entries()) {
      if (col === 0 || processed.delete(Tuple(r, c))) continue;

      const coords = Array.from(collectIsland(matrix, new Set(), r, c));
      const coordValues = coords.map(JSON.parse);
      if (coordValues.some(([cr, cc]) => isEdge(matrix, cr, cc))) processed.add(...coords);
      else for (const [cr, cc] of coordValues) matrix[cr][cc] = 0;
    }
  }

  return matrix;
}

(() => {
  const assert = require('assert');

  assert.deepStrictEqual(
    removeIslands([
      [1, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 1, 1],
      [0, 0, 1, 0, 1, 0],
      [1, 1, 0, 0, 1, 0],
      [1, 0, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ]),
    [
      [1, 0, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 1],
      [0, 0, 0, 0, 1, 0],
      [1, 1, 0, 0, 1, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ],
  );
  assert.deepStrictEqual(
    removeIslands([
      [1, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 1],
      [0, 0, 1, 1, 0, 0],
      [1, 0, 1, 1, 0, 0],
      [1, 0, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ]),
    [
      [1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1],
      [0, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ],
  );
})();
