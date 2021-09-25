/**
 * Return cartesian product of arrays, from [StackOverflow](https://stackoverflow.com/a/43053803)
 *
 * @param {any[]} first
 * @param {any[]} second
 * @param {...any[]} rest
 * @returns {any[][]}
 */
const cartesian = (() => {
  const product = (first, second) => [].concat(...first.map(one => second.map(two => [].concat(one, two))));
  const cartesian = (first, second, ...rest) => (second ? cartesian(product(first, second), ...rest) : first);
  return cartesian;
})();

/**
 * @param  {...number} values
 */
function getAbsoluteDifference(...values) {
  let diff = 0;
  for (const [i, value] of values.entries()) {
    for (const other of values.slice(i)) {
      diff += Math.abs(value - other);
    }
  }
  return diff;
}

const sum = (...values) => values.reduce((total, value) => total + value, 0);

function functionallyGetAbsoluteDifference(...values) {
  return Array.from(values.entries()).reduce(
    (diff, [i, value]) => diff + sum(...values.slice(i).map(other => Math.abs(value - other))),
    0,
  );
}

/**
 * @param  {...number[]} arrays
 * @returns {number[]}
 */
function bruteSolve(...arrays) {
  let smallest = Number.MAX_SAFE_INTEGER;
  let result = [];

  for (const product of cartesian(...arrays)) {
    const diff = getAbsoluteDifference(...product);
    if (diff < smallest) {
      smallest = diff;
      result = product;
    }
  }
  return result;
}


/**
 * @param  {...number[]} arrays
 * @returns {number[]}
 */
function functionallyBruteSolve(...arrays) {
  return cartesian(...arrays)
    .map(product => ({ product, diff: functionallyGetAbsoluteDifference(...product) }))
    .reduce(
      ({ smallest, result }, { product, diff }) =>
        diff < smallest ? { smallest: diff, result: product } : { smallest, result },
      { smallest: Number.MAX_SAFE_INTEGER, result: [] },
    ).result;
}

/**
 * @param  {...number[]} arrays
 * @returns {number[]}
 */
function efficientSolve(...arrays) {
  for (const array of arrays) array.sort((a, b) => a - b);

  const indexes = new Array(arrays.length).fill(0);

  let smallest = Number.MAX_SAFE_INTEGER;
  let result = [];
  while (indexes.every((index, i) => [index] < arrays[i].length)) {
    const values = indexes.map((index, i) => arrays[i][index]);
    if (values.every(value => value === values[0])) {
      return values;
    }

    indexes[
      values.reduce(
        ({ index, value }, currValue, i) => (currValue < value ? { index: i, value: currValue } : { index, value }),
        { index: 0, value: values[0] },
      ).index
    ] += 1;

    const diff = getAbsoluteDifference(...values);
    if (diff < smallest) {
      smallest = diff;
      result = values;
    }
  }

  return result;
}

(() => {
  const assert = require('assert');

  for (const solve of [bruteSolve, functionallyBruteSolve, efficientSolve]) {
    assert.deepStrictEqual(solve([-1, 3], [3]), [3, 3]);
    assert.deepStrictEqual(solve([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]), [28, 26]);
    assert.deepStrictEqual(solve([-8, 4, 9, 38, 15, 67], [78, 55, 91, 30, 45, -19]), [38, 45]);
    assert.deepStrictEqual(solve([1, 2, 3, 4], [6, 7, 8, 9], [3, 5, 6, 7]), [4, 6, 5]);
  }
})();
