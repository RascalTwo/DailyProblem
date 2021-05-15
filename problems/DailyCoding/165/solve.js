/**
 * For each number, return the count of numbers to the right that are smaller then it.
 *
 * @param {number[]} integers
 *
 * @returns {number}
 */
function transformToNumberOfSmallerAfter(integers){
	return [...integers.entries()].map(([index, number]) =>
		integers.slice(index).reduce((count, other) => count + (other < number), 0)
	);
}


(() => {
	const assert = require('assert');


	assert.deepStrictEqual(transformToNumberOfSmallerAfter([3, 4, 9, 6, 1]), [1, 1, 2, 1, 0])
	assert.deepStrictEqual(transformToNumberOfSmallerAfter([1, 2, 3, 4, 5]), [0, 0, 0, 0, 0])
	assert.deepStrictEqual(transformToNumberOfSmallerAfter([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
})();
