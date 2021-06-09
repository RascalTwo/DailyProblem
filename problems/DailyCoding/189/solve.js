/**
 * @param {number[]} numbers
 * @returns {number}
 */
function longestUniqueSubarrayLength(numbers){
	let best = 0;

	for (let i = 0; i < numbers.length - best; i++){
		const unique = new Set([numbers[i]]);
		for (const number of numbers.slice(i + 1)){
			if (unique.has(number)) break;
			unique.add(number);
		}
		best = Math.max(best, unique.size);
	}

	return best;
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(longestUniqueSubarrayLength([5, 1, 3, 5, 2, 3, 4, 1]), 5);
	assert.deepStrictEqual(longestUniqueSubarrayLength([1, 2, 3, 4, 5]), 5);
	assert.deepStrictEqual(longestUniqueSubarrayLength([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), 2);
	assert.deepStrictEqual(longestUniqueSubarrayLength([9, 6, 8, 1, 4, 1, 3, 2, 1, 7, 5]), 5);
})();