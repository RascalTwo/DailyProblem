function solveSet(...nums: number[]){
	return new Set(nums).size !== nums.length;
}

function solveEfficient(...nums: number[]){
	const seen = new Set();
	for (const num of nums){
		if (seen.has(num)) return true;
		seen.add(num)
	}
	return false;
}


(() => {
	const assert = require('assert');
	for (const solve of [solveSet, solveEfficient]){
		assert.deepStrictEqual(solve(1, 2, 3, 1), true);
		assert.deepStrictEqual(solve(1, 2, 3, 4), false);
		assert.deepStrictEqual(solve(1, 1, 1, 3, 3, 4, 3, 2, 4, 2), true);
	}
})();
