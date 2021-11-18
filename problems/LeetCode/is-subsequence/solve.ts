function solve(needle: string, haystack: string): boolean{
	if (!needle) return true;

	const length = needle.length;
	let i = 0
	for (const char of haystack){
		if (needle[i] === char) i++;
		if (i >= length) return true;
	}

	return i == length
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve("", "ahbgdc"), true);
	assert.deepStrictEqual(solve("a", ""), false);
	assert.deepStrictEqual(solve("", ""), true);
	assert.deepStrictEqual(solve("abc", "ahbgdc"), true);
	assert.deepStrictEqual(solve("axc", "ahbgdc"), false);
})();