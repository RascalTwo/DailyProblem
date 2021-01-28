/**
 * Remove duplicates from a sorted array of integers
 *
 * @param {number[]} integers
 * @returns {number[]}
 */
function removeSortedDupes(integers){
	for (let i = 0; i < integers.length - 1; i++){
		while (integers[i] === integers[i + 1]) integers.splice(i + 1 , 1);
	}

	return integers;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(removeSortedDupes([1, 1, 2]), [1, 2])
	assert.deepStrictEqual(removeSortedDupes([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), [0, 1, 2, 3, 4])
	assert.deepStrictEqual(removeSortedDupes([4, 4, 5, 7, 7, 7, 7, 8, 9, 10, 10, 10]), [4, 5, 7, 8, 9, 10])

})();