/**
 * @param {number} number
 * @returns {boolean}
 */
function isSparse(number){
	return !number.toString(2).includes('11');
}

/**
 * @param {number} number
 * @param {number}
 */
function nextSparseBrute(number){
	while(true){
		if (isSparse(number)) return number;
		number++
	}
}


/**
 * @param {number} number
 * @param {number}
 */
function nextSparse(number){
	const binary = Array.from('0' + number.toString(2));
	for (let i = binary.length - 1; i >= 0; i--){
		if (binary[i] === '1' && binary[i] === binary[i + 1]){
			binary[i - 1] = '1';
			for (let j = i; j < binary.length; j++) binary[j] = '0';
		}
	}
	return parseInt(binary.join(''), 2);
}


(() => {
	const assert = require('assert');
	for (const solve of [nextSparse, nextSparseBrute]){
		assert.deepStrictEqual(solve(6), 8);
		assert.deepStrictEqual(solve(4), 4);
		assert.deepStrictEqual(solve(38), 40);
		assert.deepStrictEqual(solve(21), 21);
		assert.deepStrictEqual(solve(22), 32);
		assert.deepStrictEqual(solve(44), 64);
		assert.deepStrictEqual(solve(63), 64);
	}
})();
