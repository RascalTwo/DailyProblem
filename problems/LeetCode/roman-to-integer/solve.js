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
 * @param {string} numerals
 * @returns {number}
 */
function numeralToInteger(numerals){
	let result = 0;
	let adding = true;
	numerals = numerals.split('').reverse().join('')

	let prev = null;
	for (const char of numerals){
		value = ROMAN_NUMERALS[char]
		adding = !prev || (prev && value >= prev)
		prev = value;

		result += adding ? value : -value;
	}

	return result
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(numeralToInteger('MDCLXVI'), 1666);
	assert.deepStrictEqual(numeralToInteger('XIV'), 14);
	assert.deepStrictEqual(numeralToInteger('XIII'), 13);
	assert.deepStrictEqual(numeralToInteger('XX'), 20);
	assert.deepStrictEqual(numeralToInteger('IX'), 9);
	assert.deepStrictEqual(numeralToInteger('XL'), 40);
	assert.deepStrictEqual(numeralToInteger('XXXIX'), 39);
	assert.deepStrictEqual(numeralToInteger('VIII'), 8);
	assert.deepStrictEqual(numeralToInteger('II'), 2);
	assert.deepStrictEqual(numeralToInteger('IV'), 4);
})();
