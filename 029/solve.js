/**
 * Decode run-length-encoded string
 *
 * @param {string} encoded
 *
 * @returns {string}
 */
function decode(encoded){
	result = '';

	multiplier = '';
	for (const char of encoded){
		if (char >= '0' && char <= '9'){
			multiplier += char;
		}
		else{
			result += char.repeat(Number(multiplier));
			multiplier = '';
		}
	}

	return result;
}


/**
 * Encode string with run-length encoding
 * @param {string} string
 *
 * @returns {string}
 */
function encode(string){
	if (!string) return '';

	result = '';
	duplicates = string[0];
	for (let i = 1; i < string.length; i++){
		const char = string[i];
		if (duplicates.includes(char)){
			duplicates += char;
		}
		else {
			result += `${duplicates.length}${duplicates[0]}`;
			duplicates = string[i];
		}
	}
	result += `${duplicates.length}${duplicates[0]}`;
	return result;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(encode(''), '');
	assert.deepStrictEqual(decode(''), '');

	assert.deepStrictEqual(encode('A'), '1A');
	assert.deepStrictEqual(decode('1A'), 'A');

	assert.deepStrictEqual(encode('AAA'), '3A');
	assert.deepStrictEqual(decode('3A'), 'AAA');

	assert.deepStrictEqual(encode('AAAABBBCCDAA'), '4A3B2C1D2A');
	assert.deepStrictEqual(decode('4A3B2C1D2A'), 'AAAABBBCCDAA');

	assert.deepStrictEqual(encode('BAAAAAAAAAAAAAAAB'), '1B15A1B');
	assert.deepStrictEqual(decode('1B15A1B'), 'BAAAAAAAAAAAAAAAB');
})();
