function solve(number: number){
	return number ? Math.floor(Math.log10(number > 0 ? number : -number)) + 1 : 1
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve(1), 1);
	assert.deepStrictEqual(solve(9), 1);
	assert.deepStrictEqual(solve(10), 2);
	assert.deepStrictEqual(solve(0), 1);
	assert.deepStrictEqual(solve(-10), 2);
	assert.deepStrictEqual(solve(-99), 2);
	assert.deepStrictEqual(solve(100), 3);
	assert.deepStrictEqual(solve(150), 3);
})();
