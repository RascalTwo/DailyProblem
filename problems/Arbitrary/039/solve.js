/**
 * @param {number[]} steps
 * @returns {boolean}
 */
function canReachEnd(steps){
	let i = 0;
	const seen = new Set();
	while (!seen.has(i) && i !== steps.length - 1){
		seen.add(i)
		i += steps[i]
	}
	return i == steps.length - 1;
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(canReachEnd([2, 3, 1, -2, 0]), true);
	// Positions: 0 -> 2 -> 3 -> 1 -> 4
	assert.deepStrictEqual(canReachEnd([1, 3, 1, 2, 0, 1]), false);
	assert.deepStrictEqual(canReachEnd([1, 2, 1, 0, 0]), false);
	assert.deepStrictEqual(canReachEnd([3, 1, 2, -2, 0]), true);
	assert.deepStrictEqual(canReachEnd([2, 2, -1, -3, 0]), false);
})();
