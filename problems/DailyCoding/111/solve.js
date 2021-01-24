/**
 * Return all indices in string at which word can be found as an anagram
 *
 * @param {string} word
 * @param {string} string
 *
 * @yields {number} indices
 */
function* anagramIndices(word, string){
	const searchingFor = new Set(word);
	for (let i = 0; i < string.length - word.length + 1; i++){
		if (Array.from(new Set(string.slice(i, i + word.length))).every(c => searchingFor.has(c))) yield i;
	}
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(Array.from(anagramIndices('ab', 'abxaba')), [0, 3, 4]);
})();