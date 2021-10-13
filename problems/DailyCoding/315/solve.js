/**
 * @param {number[][]} matrix
 * @returns {boolean}
 */
function solveDiagonal(matrix){
	for (let [row, col] of [
		...new Array(matrix[0].length).fill(0).map((col, row) => [col, row]),
		...new Array(matrix.length).fill(0).map((col, row) => [row, col]),
	]){
		const last = matrix[row][col];
		for (; 0 <= row && row < matrix.length && 0 <= col && col < matrix[0].length; row++, col++){
			if (matrix[row][col] != last) return false;
		}
	}

	return true;
}

function arraysAreEqual(a, b){
  for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
  return true;
}

/**
 * @param {number[][]} matrix
 * @returns {boolean}
 */
function solveIter(matrix){
	for (let i = matrix.length - 1; i > 0; i--){
		//if (JSON.stringify(matrix[i].slice(1)) !== JSON.stringify(matrix[i - 1].slice(0, -1))) return false;
		if (!arraysAreEqual(matrix[i].slice(1), matrix[i - 1].slice(0, -1))) return false;
	}
	return true;
};


/**
 * @param {number[][]} matrix
 * @returns {boolean}
 */
function solveHashing(matrix){
	const diffs = {};
	for (let i = 0; i < matrix.length; i++){
		for (let j = 0; j < matrix[i].length; j++){
			const hash = i - j;
			if (hash in diffs && diffs[hash] !== matrix[i][j]) return false;

			diffs[hash] = matrix[i][j];
		}
	}
	return true;
}


function* generateToeplitz(rows, columns){
	const values = new Array(columns).fill(undefined).map((_, v) => v);
	for (let i = 0; i < rows; i++){
		yield [...values]
		values.unshift(values.pop());
	}
}


(() => {
	const assert = require('assert');

	for (const solve of [solveDiagonal, solveIter, solveHashing]){
		assert.deepStrictEqual(solve([
			[1, 2, 3, 4, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 4, 5, 1, 2],
		]), true);
		assert.deepStrictEqual(solve([
			[0, 2, 3, 4, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 4, 5, 1, 2],
		]), false);
		assert.deepStrictEqual(solve([
			[1, 2, 3, 0, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 4, 5, 1, 2],
		]), false);
		assert.deepStrictEqual(solve([
			[1, 2, 3, 0, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 0, 5, 1, 2],
		]), false);
		assert.deepStrictEqual(solve(Array.from(generateToeplitz(1000, 1000))), true);
	}
})();
