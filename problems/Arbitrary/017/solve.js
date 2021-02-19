const isPrime = num => {
	for (let i = 2, s = Math.sqrt(num); i <= s; i++){
		if (num % i === 0) return false;
	}
	return num > 1;
}

/**
 * Return number of prime integers in the integers array
 *
 * @param {number[]} integers
 * @returns {number}
 */
function countPrimes(integers){
	return integers.reduce((count, number) => count + isPrime(number), 0);
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(countPrimes([1, 2, 3]), 2)
	assert.deepStrictEqual(countPrimes([17]), 1)
	assert.deepStrictEqual(countPrimes([4, 6, 8, 10]), 0)
	assert.deepStrictEqual(countPrimes([4, 4, 4, 13, 4, 4, 4]), 1)
	assert.deepStrictEqual(countPrimes([4, 8, 6, 2, 75, 98, 35, 14, 43, 48]), 2)
})();