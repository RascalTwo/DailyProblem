/**
 * Return if the parenthesis can be balanced when `*`'s are replaced
 *
 * @param {string} string
 */
function isBalanceable(string, opened=0){
	for (const [i, char] of Array.from(string).entries()){
		if (char === '*'){
			if ([' ', '(', ')'].some(sub => isBalanceable(sub + string.slice(i + 1), opened))) return true;
		}
		else if (char === '('){
			opened++;
		}
		else if (char === ')'){
			if (!opened) return false;
			opened--;
		}
	}

	return !opened;
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(isBalanceable('()()'), true);
	assert.deepStrictEqual(isBalanceable('()'), true);
	assert.deepStrictEqual(isBalanceable('((()'), false);
	assert.deepStrictEqual(isBalanceable(')'), false);
	assert.deepStrictEqual(isBalanceable('(())'), true);
	assert.deepStrictEqual(isBalanceable('(()*'), true);
	assert.deepStrictEqual(isBalanceable('(*)'), true);
	assert.deepStrictEqual(isBalanceable(')*('), false);
	assert.deepStrictEqual(isBalanceable('(**'), true);
	assert.deepStrictEqual(isBalanceable('((**'), true);
	assert.deepStrictEqual(isBalanceable('()**'), true);
	assert.deepStrictEqual(isBalanceable('((*)('), false);
	assert.deepStrictEqual(isBalanceable('((*'), false);
})();
