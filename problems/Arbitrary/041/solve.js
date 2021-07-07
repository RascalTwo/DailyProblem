/**
 * @param {string} term
 * @returns {string}
 */
function nextTerm(term){
	const counts = [];
	let index = 0;
	let count = 1;
	for (let i = 1; i < term.length; i++){
		if (term[i] === term[index]) count++
		else {
			counts.push([count, term[index]])
			index = i
			count = 1
		}
	}
	if (count) counts.push([count, term[index]])

	term = '';
	for (const [count, character] of counts.reverse()){
		term = count.toString() + character + term;
	}
	return term;
}


/**
 * @param {string} term
 * @param {number} n
 * @yields {string}
 */
function* nextTerms(term, n){
	for (let i = 0; i < n; i++){
		term = nextTerm(term)
		yield term;
	}
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(nextTerm('1223334444'), '11223344');
	assert.deepStrictEqual(Array.from(nextTerms('2', 7)), ['12', '1112', '3112', '132112', '1113122112', '311311222112', '13211321322112']);
})();