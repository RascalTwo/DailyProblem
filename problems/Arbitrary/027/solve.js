/**
 * Return if the letter string can be constructed from the characters in newspaper.
 *
 * @param {string} letter String desired to be constructed
 * @param {string} newspaper Pool of available characters
 *
 * @returns If letter can be constructed with the characters from the newspaper
 */
function canConstructString(letter, newspaper){
	const counts = [...letter].reduce((counts, char) => {
		if (!(char in counts)) counts[char] = 0;
		counts[char] += 1;
		return counts;
	}, {});
	const poolCounts = [...newspaper].reduce((counts, char) => {
		if (!(char in counts)) counts[char] = 0;
		counts[char] += 1;
		return counts;
	}, {});

	for (const [char, needed] of Object.entries(counts)){
		if (!(char in poolCounts)) return false;
		if (poolCounts[char] < needed) return false;
	}
	return true;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(canConstructString('abc', 'euokdcba'), true);
	assert.deepStrictEqual(canConstructString('abc', 'aabbcc'), true);
	assert.deepStrictEqual(canConstructString('hello world!', ' !dehllloorw'), true);
	assert.deepStrictEqual(canConstructString('hello world!', ' !dehlloorw'), false);
	assert.deepStrictEqual(canConstructString('hello world!', ' abc'), false);
})();