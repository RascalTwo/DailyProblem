/**
 * Zipper merge strings into a single string
 *
 * @param  {...string} strings
 *
 * @returns {string}
 */
function merge(...strings){
	let result = ''

	for (let i = 0; i < strings[0].length; i++){
		for (let string of strings){
			result += string[i];
		}
	}

	return result;
}


/**
 * Split merged string into k words
 *
 * @param {string} string
 * @param {number} k
 *
 * @returns {string[]}
 */
function split(string, k){
	if (string.length % k !== 0) throw new Error(`"${string}" can not be evenly broken into ${k} words`)

	let words = Array(k).fill('');

	for (const [i, char] of [...string].entries()){
		words[i % k] += char;
	}

	return words;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(merge('ABC', '123'), 'A1B2C3')
	assert.deepStrictEqual(merge('hello', 'world'), 'hweolrllod')
	assert.deepStrictEqual(merge('---', '===', '___'), '-=_-=_-=_')

	for (const string of ['1234567', '12345']){
			assert.throws(() => split(string, 6), { message: `"${string}" can not be evenly broken into 6 words` });
	}

	assert.deepStrictEqual(split('A1B2C3', 2), ['ABC', '123'])
	assert.deepStrictEqual(split('hweolrllod', 2), ['hello', 'world'])
	assert.deepStrictEqual(split('-=_-=_-=_', 3), ['---', '===', '___'])
})();