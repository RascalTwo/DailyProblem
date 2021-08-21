/**
 * Return the fixed point in the array
 *
 * @param {number[]} integers
 *
 * @returns {number}
 */
function fixedPointOf(integers){
	for (const [index, value] of integers.entries()){
		if (index === value) return index;
	}
	return -1;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(fixedPointOf([7, 8, 5, 2, 4, 9]), 4);
	assert.deepStrictEqual(fixedPointOf([7, 8, 5, 2, 8, 9]), -1);
	assert.deepStrictEqual(fixedPointOf([-6, 0, 2, 40]), 2);
	assert.deepStrictEqual(fixedPointOf([1, 5, 7, 8]), -1);
})();