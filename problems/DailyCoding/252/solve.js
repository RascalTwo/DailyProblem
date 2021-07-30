/**
 * @param {number} goal
 * @yields {number}
 */
function* generateEgyptianDenominators(goal){
	let value = 0;

	let denominator = 1;
	while (value < goal){
		const change = 1 / ++denominator;
		value += change;
		if (value > goal) value -= change;
		else yield denominator
	}
}

(() => {
	const assert = require('assert');


	assert.deepStrictEqual(Array.from(generateEgyptianDenominators(5 / 8)),  [2, 8]);
	assert.deepStrictEqual(Array.from(generateEgyptianDenominators(13 / 12)),  [2, 3, 4]);
	assert.deepStrictEqual(Array.from(generateEgyptianDenominators(4 / 13)),  [4, 18, 468]);
})();