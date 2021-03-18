/**
 * Return if two numbers in numbers can be added together and equal goal
 *
 * @param {number[]} numbers
 * @param {number} goal
 *
 * @returns If two numbers in numbers summed equaled goal
 */
function anyEqualIter(numbers, goal){
	for (let i = 0; i < numbers.length - 1; i++){
		for (let j = i + 1; j < numbers.length; j++){
			if (numbers[i] + numbers[j] == goal) return true;
		}
	}

	return false;
}


/**
 * Return if two numbers in numbers can be added together and equal goal
 *
 * @param {number[]} numbers
 * @param {number} goal
 *
 * @returns If two numbers in numbers summed equaled goal
 */
function anyEqualMap(numbers, goal){
	const others = new Set();

	for (const value of numbers){
		if (others.has(value)) return true;
		others.add(goal - value);
	}

	return false;
}


/**
 * Return if two numbers in numbers can be added together and equal goal
 *
 * @param {number[]} numbers
 * @param {number} goal
 *
 * @returns If two numbers in numbers summed equaled goal
 */
function anyEqualPointers(numbers, goal){
	numbers.sort();

	let i = 0;
	let j = numbers.length - 1;

	while (i < j){
		const [a, b] = [numbers[i], numbers[j]];
		const total = a + b;
		if (total == goal) return true;
		if (total > goal){
			if (a > b){
				i++;
			}
			else {
				j--
			}
		}
		else{
			if (a < b){
				i++;
			}
			else {
				j--
			}
		}
	}

	return false;
}


(() => {
	const assert = require('assert');

	for (const anyEqual of [anyEqualIter, anyEqualMap, anyEqualPointers]){
		assert.deepStrictEqual(anyEqual([10, 15, 3, 7], 17), true);
		assert.deepStrictEqual(anyEqual([9, 4, 3, 6], 39), false);
		assert.deepStrictEqual(anyEqual([7, 3, 15, 10], 17), true);
		assert.deepStrictEqual(anyEqual([1, 2], 3), true);
		assert.deepStrictEqual(anyEqual([1], 3), false);
		assert.deepStrictEqual(anyEqual([1, 4, 9, 6], 10), true);
		assert.deepStrictEqual(anyEqual([1, 7, 4, 8, 6, 7], 12), true);
		assert.deepStrictEqual(anyEqual([2, 7, 11, 15], 9), true);
		assert.deepStrictEqual(anyEqual([3, 2, 4], 6), true);
		assert.deepStrictEqual(anyEqual([3, 3], 6), true);
	}
})();
