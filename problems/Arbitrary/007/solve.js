/**
 * Inverse the case of the given string
 *
 * @param {string} string
 *
 * @returns {string}
 */
function invertCase(string){
	return [...string].map(char => char.toUpperCase() === char ? char.toLowerCase() : char.toUpperCase()).join('');
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(invertCase('hello world'), 'HELLO WORLD')
	assert.deepStrictEqual(invertCase('AbCdEf'), 'aBcDeF')
})();