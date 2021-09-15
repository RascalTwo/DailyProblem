/**
 * @param {number} number
 * @returns {number}
 */
function getMostBinaryOnes(number) {
  let longest = 0;
  let current = 0;
  for (const char of number.toString(2)) {
    if (char === '1') current += 1;
    else {
      longest = Math.max(longest, current);
      current = 0;
    }
  }

  return Math.max(longest, current);
}

/**
 * @param {number} number
 * @returns {number}
 */
function functionallyGetMostBinaryOnes(number) {
  return Array.from(number.toString(2)).reduce(
    ({ longest, current: previous }, char) => {
      const current = char === '1' ? previous + 1 : 0;
      return { longest: Math.max(longest, current), current };
    },
    { longest: 0, current: 0 },
  ).longest;
}

(() => {
  const assert = require('assert');

  for (const solve of [getMostBinaryOnes, functionallyGetMostBinaryOnes]) {
    assert.deepStrictEqual(solve(156), 3);
    assert.deepStrictEqual(solve(1), 1);
    assert.deepStrictEqual(solve(3), 2);
    assert.deepStrictEqual(solve(7), 3);
    assert.deepStrictEqual(solve(15), 4);
    assert.deepStrictEqual(solve(31), 5);
    assert.deepStrictEqual(solve(63), 6);
  }
})();
