/**
 * Return if the difference between the provided integers is constant
 *
 * @param  {...number} integers
 *
 * @returns {boolean}
 */
function isLinear(...integers){
	if (integers.length <= 2) return true;
	const diff = Math.abs(integers[0] - integers[1]);
	return integers.slice(1, -1).every((v, i) => Math.abs(v - integers[i + 2]) === diff);
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(isLinear(), true);
	assert.deepStrictEqual(isLinear(1), true);
	assert.deepStrictEqual(isLinear(1, 2, 3), true);
	assert.deepStrictEqual(isLinear(-1, -2, -3), true);
	assert.deepStrictEqual(isLinear(-1, 0, 1), true);
	assert.deepStrictEqual(isLinear(0, 2, 4, 6, 8, 10), true);
	assert.deepStrictEqual(isLinear(0, 1.5, 3, 4.5, 6), true);
	assert.deepStrictEqual(isLinear(1, 2, 3, 2, 1), true);
	assert.deepStrictEqual(isLinear(1, 3, 2), false);
	assert.deepStrictEqual(isLinear(2, 1, 3), false);
})();