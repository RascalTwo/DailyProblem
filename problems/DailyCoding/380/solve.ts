function solve(product: number, divisor: number): [number, number]{
	let dividend = 0;
	while (product > divisor) {
		dividend++;
		product -= divisor
	}
	return [dividend, product];
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve(10, 3), [3, 1]);
})();