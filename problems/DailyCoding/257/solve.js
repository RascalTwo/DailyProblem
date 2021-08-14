/**
 * @param {number[]} numbers
 * @return {[number, number]}
 */
function bruteForce(numbers){
	const goal = numbers.slice().sort();

	/** @type {[number, number]} */
	let bestWindow = [0, numbers.length - 1];
	for (let i = 0; i < numbers.length - 1; i++){
		for (let j = i + 1; j < numbers.length; j++){
			const sortedWindow = numbers.slice(i, j + 1).sort()
			if (numbers.slice(i, j + 1).toString() === sortedWindow.toString()) continue;

			const attempt = numbers.slice();
			attempt.splice(i, j - i + 1, ...sortedWindow)
			if (attempt.toString() === goal.toString() && j - i < bestWindow[1] - bestWindow[0]){
				bestWindow = [i, j];
			}
		}
	}

	return bestWindow;
}

/**
 * @param {number[]} numbers
 * @return {[number, number]}
 */
function twoPointers(numbers){
	let leftIndex = -1;
	let rightIndex = -1;

	let maximum = Number.MIN_SAFE_INTEGER;
	for (let i = 0; i < numbers.length; i++){
		if (maximum < numbers[i]) maximum = numbers[i];

		if (numbers[i] < maximum) rightIndex = i;
	}

	let minimum = Number.MAX_SAFE_INTEGER;
	for (let i = numbers.length; i >= 0; i--){
		if (minimum > numbers[i]) minimum = numbers[i];

		if (numbers[i] > minimum) leftIndex = i;
	}

	return [leftIndex, rightIndex];
}

(() => {
	const assert = require('assert');

	for (const solve of [bruteForce, twoPointers]){
		assert.deepStrictEqual(solve([3, 7, 5, 6, 9]), [1, 3]);
		assert.deepStrictEqual(solve([9, 8, 7, 6, 5, 4]), [0, 5])
		assert.deepStrictEqual(solve([1, 2, 3, 5, 4, 6, 8, 7, 9]), [3, 7])
	}
})();