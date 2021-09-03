/**
 * @param {number} number
 * @yields {number}
 */
function* getKaprekarConstantIntermediates(number){
	while(true){
		const ascending = Array.from(number.toString()).sort();
		let first = ascending.join('');
		let second = ascending.reverse().join('')
		if (first < second){
			([first, second] = [second, first]);
		}
		number = Number(first) - Number(second);
		if (number === 6174) break;
		yield number;
	}
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(Array.from(getKaprekarConstantIntermediates(1234)), [3087, 8352]);
	assert.deepStrictEqual(Array.from(getKaprekarConstantIntermediates(1495)), [8082, 8532]);
	assert.deepStrictEqual(Array.from(getKaprekarConstantIntermediates(6451)), [5085, 7992, 7173, 6354, 3087, 8352]);
})();
