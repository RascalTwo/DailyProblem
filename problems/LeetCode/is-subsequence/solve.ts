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

function* solveMass(haystack: string, ...needles: string[]): Generator<boolean, any, any>{
	const indexes: Record<string, number[]> = {}
	for (const [i, char] of Array.from(haystack).entries()){
		if (!(char in indexes)) indexes[char] = []
		indexes[char].push(i)
	}

	for (const needle of needles){
		let last: number | null = null
		let i = 0;
		for (const char of needle){
			if (!(char in indexes)) break;
			let found = indexes[char].find(index => index > (last ?? -1));
			if (found === undefined) break;
			last = found;
			i++;
		}
		yield i === needle.length;
	}
}
function* bruteMass(haystack: string, ...needles: string[]): Generator<boolean, any, any>{
	for (const needle of needles){
		yield solve(needle, haystack);
	}
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve("", "ahbgdc"), true);
	assert.deepStrictEqual(solve("a", ""), false);
	assert.deepStrictEqual(solve("", ""), true);
	assert.deepStrictEqual(solve("abc", "ahbgdc"), true);
	assert.deepStrictEqual(solve("axc", "ahbgdc"), false);


	const haystack = 'a'.repeat(1000000) + 'abcdefghijklmnopqrstuvwxyz';
	const needles = new Array(50).fill(undefined).map(() => ['adjquv', 'adjqua', 'adjquvz', 'adjquva']).flat();
	const results = [...new Array(50).fill(undefined).map(() => [true, false, true, false]).flat(), true];
	for (const massSolver of [solveMass, bruteMass]){
		assert.deepStrictEqual(Array.from(massSolver(haystack, ...needles, 'bdfh')), results);
	}
})();