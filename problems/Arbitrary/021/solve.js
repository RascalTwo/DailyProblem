/**
 * Return a mapping between the characters in the strings and the indexes they appear
 * @param {string} string
 *
 * @returns {{[key as string]: number[]}}
 */
function getCharacterIndexes(string){
	const indexes = {};
	for (const [i, char] of [...string].entries()){
		if (!indexes[char]) indexes[char] = []
		indexes[char].push(i);
	}
	return indexes;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(getCharacterIndexes('abc  cba'), {a: [0, 7], b: [1, 6], c: [2, 5], ' ': [3, 4]});

	assert.deepStrictEqual(getCharacterIndexes('hello, world!'), {
		h: [0 ],
		e: [1 ],
		l: [2, 3, 10],
		o: [4, 8],
		',': [5],
		' ': [6],
		w: [7],
		r: [9],
		d: [11],
		'!': [12]
	});
})();