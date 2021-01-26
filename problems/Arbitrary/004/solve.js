/**
 * Return if the string is an isogram - has no repeating characters
 *
 * @param {string} string
 *
 * @returns {boolean} if the string is an isogram
 */
function isIsogram(string){
	return new Set(string).size === string.length;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(isIsogram('isogram'), true);
	assert.deepStrictEqual(isIsogram('heterogram'), false);
})();
