const ROMAN_NUMERALS = {
	M: 1000,
	CM: 900,
	D: 500,
	CD: 400,
	C: 100,
	XC: 90,
	L: 50,
	XL: 40,
	X: 10,
	IX: 9,
	V: 5,
	IV: 4,
	I: 1
}


/**
 * @param {number} integer
 * @returns {string}
 */
function integerToNumeral(integer){
	let numerals = '';

	for (const [symbol, value] of Object.entries(ROMAN_NUMERALS)){
		numerals += symbol.repeat(Math.floor(integer / value))
		integer %= value;
	}

	return numerals;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(integerToNumeral(1666), 'MDCLXVI');
	assert.deepStrictEqual(integerToNumeral(14), 'XIV');
	assert.deepStrictEqual(integerToNumeral(13), 'XIII');
	assert.deepStrictEqual(integerToNumeral(20), 'XX');
	assert.deepStrictEqual(integerToNumeral(9), 'IX');
	assert.deepStrictEqual(integerToNumeral(40), 'XL');
	assert.deepStrictEqual(integerToNumeral(39), 'XXXIX');
	assert.deepStrictEqual(integerToNumeral(8), 'VIII');
	assert.deepStrictEqual(integerToNumeral(2), 'II');
	assert.deepStrictEqual(integerToNumeral(4), 'IV');
})();