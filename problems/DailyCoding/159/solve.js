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


/**
 * Return the first character that is repeated in the string
 *
 * @param {string} string
 *
 * @returns {string | null}
 */
const getFirstRepeatingES6 = (string) => (res = Array.from(string).reduce((seen, char, _, arr) => {
	if (!seen.has(char)) return new Set([...seen, char]);

	arr.splice(0);
	return char;
}, new Set())) instanceof Set ? null : res;


(() => {
	const assert = require('assert');

	for (const solve of [getFirstRepeating, getFirstRepeatingES6]){
		assert.deepStrictEqual(solve('acbbac'), 'b');
		assert.deepStrictEqual(solve('abcdef'), null);
		assert.deepStrictEqual(solve('ewkdfooie'), 'o');
	}
})();
