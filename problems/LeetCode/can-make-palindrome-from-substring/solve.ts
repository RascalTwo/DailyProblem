type Query = [number, number, number];

function attemptReplacement(string: string, start: number, replacements: number): boolean {
	if (string.length === 1 || replacements >= Math.floor(string.length / 2)) return true;
	const counts = Array.from(string).reduce((counts, char) => ({
		...counts,
		[char]: (counts[char] ?? 0) + 1
	}), {} as Record<string, number>);

	const odds = Object.entries(counts).filter(item => item[1] % 2);

	let isPalindrome = string.length % 2 === 0
		? !Object.values(counts).some(count => count % 2)
		: odds.length === 1;
	if (isPalindrome) return true;
	if (odds.length === 1) return false;
	if (!replacements) return false;

	const char = odds[0][0];
	const i = string.indexOf(char);
	const other = odds[1][0];
	if (attemptReplacement(string.substring(0, i) + other + string.substring(i + 1), start, replacements - 1)) return true;

	return false;
}

function* solve(haystack: string, ...queries: Query[]): Generator<boolean, any, any> {
	for (const [left, right, replacements] of queries) {
		const substring = haystack.substring(left, right + 1);
		yield attemptReplacement(substring, 0, replacements);
	}
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(Array.from(solve('abcda', [3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1])), [true, false, false, true, true]);
	assert.deepStrictEqual(Array.from(solve('lyb', [0, 1, 0], [2, 2, 1])), [false, true]);
	assert.deepStrictEqual(Array.from(solve('rkzavgdmdgt', [5, 8, 0], [7, 9, 1], [3, 6, 4], [5, 5, 1], [8, 10, 0], [3, 9, 5], [0, 10, 10], [6, 8, 3])), [false, true, true, true, false, true, true, true]);
	assert.deepStrictEqual(Array.from(solve('hunu', [1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 2], [1, 3, 3], [2, 3, 1], [3, 3, 1], [0, 3, 0], [1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 1], [1, 1, 1])), [true, false, true, true, true, true, true, false, true, false, true, true, true]);
	assert.deepStrictEqual(Array.from(solve('pqtadspgvinafefk', [1, 14, 5], [14, 15, 1], [15, 15, 1])), [true, true, true]);
	assert.deepStrictEqual(Array.from(solve('abc', [0, 2, 0])), [false]);
})();