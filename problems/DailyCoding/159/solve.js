/**
 * Return the first character that is repeated in the string
 *
 * @param {string} string
 *
 * @returns {string | null}
 */
function getFirstRepeating(string){
	const seen = new Set();
	for (const letter of string){
		if (seen.has(letter)) return letter;
		seen.add(letter);
	}

	return null;
}


(() => {
	const assert = require('assert');


	assert.deepStrictEqual(getFirstRepeating('acbbac'), 'b');
	assert.deepStrictEqual(getFirstRepeating('abcdef'), null);
	assert.deepStrictEqual(getFirstRepeating('ewkdfooie'), 'o');
})();
