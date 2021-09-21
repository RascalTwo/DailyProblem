/**
 * @param {number[]} array
 * @returns {number}
 */
const sum = array => array.reduce((total, value) => total + value, 0);


/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveLoops(numbers){
	for (let i = 1; i < numbers.length - 1; i++){
		let leftSum = 0;
		let rightSum = 0;

		let position = i;
		while(numbers[position - 1] !== undefined){
			leftSum += numbers[position - 1];
			position--;
		}
		for (let position = i; numbers[position + 1] !== undefined; position++){
			rightSum += numbers[position + 1];
		}
		if (leftSum === rightSum) return i;
	}
}

/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveIter(numbers){
	for (let i = 1; i < numbers.length - 1; i++){
		if (sum(numbers.slice(0, i)) == sum(numbers.slice(i + 1))) return i;
	}
}


/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveCenterIter(numbers){
	const tried = new Set();
	let pivot = Math.floor(numbers.length / 2)
	while (!tried.has(pivot)){
		tried.add(pivot)
		const diff = sum(numbers.slice(0, pivot)) - sum(numbers.slice(pivot + 1))
		if (diff == 0) return pivot;
		pivot += diff > 0 ? -1 : 1
	}
}


/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveCenterEfficientArrays(numbers){
	const tried = new Set();
	let pivot = Math.floor(numbers.length / 2);
	const left = numbers.slice(0, pivot);
	const right = numbers.slice(pivot + 1);
	while (!tried.has(pivot)){
		tried.add(pivot)
		const diff = sum(left) - sum(right)
		if (diff == 0) return pivot;
		else if (diff < 0){
			left.push(numbers[pivot]);
			right.shift();
			pivot += 1;
		}
		else{
			right.push(numbers[pivot]);
			left.pop();
			pivot -= 1;
		}
	}
}


/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveCenterArrayless(numbers){
	const tried = new Set();
	let pivot = Math.floor(numbers.length / 2);
	let leftSum = sum(numbers.slice(0, pivot));
	let rightSum = sum(numbers.slice(pivot + 1));
	while (!tried.has(pivot)){
		tried.add(pivot)
		if (leftSum === rightSum) return pivot;
		else if (leftSum < rightSum){
			leftSum += numbers[pivot];
			pivot += 1;
			rightSum -= numbers[pivot];
		}
		else{
			rightSum += numbers[pivot]
			pivot -= 1;
			leftSum -= numbers[pivot]
		}
	}
}

/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveCenterDiff(numbers){
	const tried = new Set();
	let pivot = Math.floor(numbers.length / 2);
	let diff = sum(numbers.slice(0, pivot)) - sum(numbers.slice(pivot + 1))
	while (!tried.has(pivot)){
		tried.add(pivot)
		if (!diff) return pivot;
		else if (diff < 0){
			diff += numbers[pivot]
			pivot += 1;
			diff += numbers[pivot]
		}
		else{
			diff -= numbers[pivot]
			pivot -= 1;
			diff -= numbers[pivot]
		}
	}
}

/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveTwoPointer(numbers){
	let left = 0;
	let leftSum = 0;

	let right = numbers.length - 1;
	let rightSum = 0;

	while (left < right){
		leftSum += numbers[left];
		rightSum += numbers[right]
		while (leftSum !== rightSum && left < right){
			if (leftSum < rightSum) leftSum += numbers[++left];
			else if (rightSum < leftSum) rightSum += numbers[--right];
		}

		left++;
		right--;
	}

	if (leftSum === rightSum && left == right) return left;
}


/**
 * @param {number[]} numbers
 * @returns {number}
 */
function solveTwoPointerDiff(numbers){
	let left = 0;

	let right = numbers.length - 1;

	let diff = 0;
	while (left < right){
		diff += numbers[left] - numbers[right];
		while (diff && left < right){
			if (diff < 0) diff += numbers[++left];
			else diff -= numbers[--right];
		}

		left++;
		right--;
	}

	if (diff === 0 && left == right) return left;
}

(() => {
	const assert = require('assert');


	for (const solve of [solveLoops, solveIter, solveCenterIter, solveCenterEfficientArrays, solveCenterArrayless, solveCenterDiff, solveTwoPointer, solveTwoPointerDiff]){
		assert.deepStrictEqual(solve([1, 2, 3, 3]), 2);
		assert.deepStrictEqual(solve([3, 1, 2, 1]), 1);
		assert.deepStrictEqual(solve([3, 1, 3, 1]), undefined);
		assert.deepStrictEqual(solve([10, 4, 9, 1]), 1);
		assert.deepStrictEqual(solve([10, 4, 1, 9, 1, 3, 1]), 2);
		assert.deepStrictEqual(solve([10, 10, 10, 10, 10, 9, 50]), 5);
		assert.deepStrictEqual(solve([14, 13, 17, 13, 9, 18, 17, 20, 14, 13, 2, 15, 8, 2, 20, 14, 19, 16, 2, 10]), 8);
		assert.deepStrictEqual(solve([13, 2, 8, 14, 15, 10, 3, 16, 8, 15, 12, 20, 15, 16, 1, 7, 5, 20, 12, 8]), 10);
		assert.deepStrictEqual(solve([40, 40, 39, 36, 31, 26, 25, 25, 23, 22, 20, 19, 16, 16, 15, 14, 14, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 10, 10, 9, 9, 7, 6, 6, 6, 5, 5, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0]), 10);
		assert.deepStrictEqual(solve([0, 1, 0, 3, 0, 5, 0, 2, 0, 7, 8, 7, 0, 0, 3, 11, 4, 17, 16, 6, 19, 8, 0, 10, 22, 8, 12, 9, 21, 19, 28, 8, 3, 9, 18, 34, 29, 31, 29, 38, 38, 22, 42, 36, 19, 31, 33, 42, 37, 40]), 38);
	}
})();