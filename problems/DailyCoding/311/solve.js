/**
 * @param {number[]} numbers
 * @returns {number}
 */
function findPeak(numbers){
	let peak = -1;
	let bestSlope = 0;
	for (const [i, number] of numbers.slice(1, -1).entries()){
		let [left, right] = [numbers[i + 1 - 1], numbers[i + 1 + 1]];
		if (number < left || number < right) continue;
		const slope = (number - left) + (number - right);
		if (slope > bestSlope){
			[peak, bestSlope] = [i + 1, slope];
		}
	}

	return peak;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(findPeak([1, 2, 3, 1]), 2);
	assert.deepStrictEqual(findPeak([1, 2, 3, 4]), -1);
	assert.deepStrictEqual(findPeak([8, 7, 6, 1, 4, 5, 3, 9, 8, 4]), 7);
})();
