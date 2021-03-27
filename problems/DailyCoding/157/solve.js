/**
 * Return if the string can rearranged into a palindrome
 *
 * @param {string} string
 *
 * @returns {boolean}
 */
function canBePalindrome(string){
	return Object.values(Array.from(string)
		.map(char => char.trim().toLowerCase())
		.filter(Boolean)
		.reduce((counts, char) => {
		if (!(char in counts)) counts[char] = 0;
		counts[char] += 1
		return counts;
	}, {})).filter(count => count % 2 === 1).length <= 1;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(canBePalindrome('carrace'), true);
	assert.deepStrictEqual(canBePalindrome('daily'), false);
	assert.deepStrictEqual(canBePalindrome('abccba'), true);
	assert.deepStrictEqual(canBePalindrome('abcdcba'), true);
	assert.deepStrictEqual(canBePalindrome('aaabbbab'), true);
	assert.deepStrictEqual(canBePalindrome('abcdcb'), false);
	assert.deepStrictEqual(canBePalindrome('atsts'), true);
	assert.deepStrictEqual(canBePalindrome('dog geese Do see'), true);
})();