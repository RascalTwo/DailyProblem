/**
 * Flood fill matrix, filling 1's to 2's
 *
 * @param {number[][]} matrix
 * @param {number} r
 * @param {number} c
 */
function floodFill(matrix, r, c){
	if (matrix[r]?.[c] !== 1) return;

	matrix[r][c] = 2;

	floodFill(matrix, r-1, c);
	floodFill(matrix, r, c-1);
	floodFill(matrix, r, c+1);
	floodFill(matrix, r+1, c);
}

/**
 * Return the number of groups of `1`s in the 2D matrix
 *
 * @param {number[][]} matrix
 *
 * @returns {number} number of groups of `1`s
 */
function countIslands(matrix){
	let islands = 0;
	for (const [r, row] of matrix.entries()){
		for (const [c, col] of row.entries()){
			if (col !== 1) continue;
			floodFill(matrix, r, c);
			islands += 1;
		}
	}

	return islands;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(countIslands([]), 0);

	assert.deepStrictEqual(countIslands([[1]]), 1);
	assert.deepStrictEqual(countIslands([[1, 0, 1]]), 2);

	assert.deepStrictEqual(countIslands([
		[1, 0, 0, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[1, 1, 0, 0, 1],
		[1, 1, 0, 0, 1]
	]), 4);
})();