/**
 * @param {any[]} array
 * @yields {any}
 */
function* permutationsOf(permutation){
	const length = permutation.length;
	const c = new Array(length).fill(0)
	let i = 1, k, p;
	yield permutation.slice();

	while (i < length) {
		if (c[i] < i) {
			k = i % 2 && c[i];
			p = permutation[i];
			permutation[i] = permutation[k];
			permutation[k] = p;
			++c[i];
			i = 1;
			yield permutation.slice();
		} else {
			c[i] = 0;
			++i;
		}
	}
}

/**
 * @param {number} number
 * @returns {number}
 */
function solve(number){
	let best = [number, Number.MAX_SAFE_INTEGER];
	for (const permutation of permutationsOf(number.toString().split(''))){
		const value = parseInt(permutation.join(''))
		const diff = value - number;
		if (diff > 0 && diff < best[1]) best = [value, diff]
	}
	return best[0];
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve(123), 132);
	assert.deepStrictEqual(solve(978), 987);
	assert.deepStrictEqual(solve(654), 654);
	assert.deepStrictEqual(solve(48975), 49578);
})();
