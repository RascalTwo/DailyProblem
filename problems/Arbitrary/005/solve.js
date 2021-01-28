/**
 * Return if two arrays of primitives contain the same elements
 *
 * @param {any[]} a
 * @param {any[]} b
 *
 * @returns {boolean} if the two arrays contain the same elements
 */
function primitiveArraysEqual(a, b){
	const aSet = new Set(a);
	const bSet = new Set(b);
	return aSet.size === bSet.size && [...aSet].every(v => bSet.has(v));
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(primitiveArraysEqual(['a', 'b'], ['b', 'a']), true);
	assert.deepStrictEqual(primitiveArraysEqual([null, false], [false, null]), true);

	assert.deepStrictEqual(primitiveArraysEqual(['a', 5], ['b', 5]), false);
	assert.deepStrictEqual(primitiveArraysEqual(['a', 'b', 'c'], ['a', 'b']), false);
	assert.deepStrictEqual(primitiveArraysEqual(['a', 'b'], ['a', 'b', true]), false);
})();
