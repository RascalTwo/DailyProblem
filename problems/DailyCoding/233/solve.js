/**
 * @param {number} n
 * @returns {number}
 */
function fibonacci(n){
	const values = [0, 1];

	for (let i = 0; i < n - 1; i++){
		values.push(values.shift() + values[0]);
	}

	return values[0];
}

(() => {
	const assert = require('assert');

	for (const [index, value] of [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].entries()){
		assert.deepStrictEqual(fibonacci(index + 1), value);
	}
})();