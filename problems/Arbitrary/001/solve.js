/**
 * @param  {...number} heights
 * @return {[number, number]}
 */
function getLargestArea(...heights){
	let left = 0;
	let right = heights.length - 1;
	let best = [[left, right], 0];
	while (left < right) {
		const area = Math.min(heights[left], heights[right]) * (right - left);
		if (area > best[1]) best = [[left, right], area];

		if (heights[left] < heights[right]) left++
		else right--;
	}

	return best[0];
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(getLargestArea(1, 8, 6, 2, 5, 4, 8, 3, 7), [1, 8]);
	assert.deepStrictEqual(getLargestArea(1, 1), [0, 1]);
	assert.deepStrictEqual(getLargestArea(4, 3, 2, 1, 4), [0, 4]);
	assert.deepStrictEqual(getLargestArea(1, 2, 1), [0, 2]);
})();