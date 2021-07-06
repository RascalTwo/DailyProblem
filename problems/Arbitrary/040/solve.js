/**
 * Given an string of characters, ensure no consecutive duplicate characters existing by removing both offending characters.
 *
 * @param {string} string
 * @returns {string}
 */
function removeConsecutiveDuplicates(string){
	for (let i = 0; i < string.length - 1; i++){
		const j = i + 1;
		if (string[i] === string[j]){
			string = string.substring(0, i) + string.substring(j + 1);
			i -= 2;
		}
	}
	return string;
}

/**
 * @param {string} string
 * @returns {string}
 */
function removeConsecutiveDuplicates(string){
	const chars = Array.from(string)
	for (let i = 0; i < chars.length - 1; i++){
		const j = i + 1;
		if (chars[i] === chars[j]){
			chars.splice(i, 2);
			i -= 2;
		}
	}
	return chars.join('');
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(removeConsecutiveDuplicates('abbc'), 'ac');
	assert.deepStrictEqual(removeConsecutiveDuplicates('abccbc'), 'ac');
	assert.deepStrictEqual(removeConsecutiveDuplicates('abbbbc'), 'ac');
	assert.deepStrictEqual(removeConsecutiveDuplicates('abbbc'), 'abc');
})();