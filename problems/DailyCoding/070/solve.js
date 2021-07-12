
/**
 * @param {number} n
 * @returns {number}
 */
function getNthPerfect(n){
	let perfect = 0;

	for (let i = 0; i < n; i++){
		do perfect++;
		while (perfect.toString().split('').reduce((sum, char) => sum + Number(char), 0) != 10);
	}

	return perfect;
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(getNthPerfect(1), 19);
	assert.deepStrictEqual(getNthPerfect(2), 28);
	assert.deepStrictEqual(getNthPerfect(3), 37);
	assert.deepStrictEqual(getNthPerfect(9), 91);
	assert.deepStrictEqual(getNthPerfect(10), 109);
	assert.deepStrictEqual(getNthPerfect(11), 118);
})();