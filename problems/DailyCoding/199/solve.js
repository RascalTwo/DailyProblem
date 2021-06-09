/**
 * Given a string containing unbalanced parenthesis, return the string with the parenthesis balanced without removing any.
 *
 * @param {string} parenthesis
 * @returns {string}
 */
function balanceParenthesis(parenthesis){
	let opened = 0;
	let i = 0;
	while (i != parenthesis.length){
		if (parenthesis[i] == '('){
			opened++;
			i++;
			continue
		}

		if (opened === 0){
			parenthesis = parenthesis.slice(0, i) + '(' + parenthesis.slice(i);
			i += 2;
		}
		else{
			opened--;
			i++;
		}
	}

	return parenthesis + ')'.repeat(opened);
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(balanceParenthesis('(()'), '(())');
	assert.deepStrictEqual(balanceParenthesis('))()('), '()()()()');
})();
