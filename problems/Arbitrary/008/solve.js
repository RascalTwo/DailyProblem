/**
 * Capitalize all words in the given string
 *
 * @param {string} string
 *
 * @returns {string}
 */
function capitalizeWords(string){
	const chars = string.split('');
	for (let i = 0; i < chars.length; i++){
		if (!i || !chars[i - 1].trim()){
			chars[i] = chars[i].toUpperCase();
		}
	}

	return chars.join('');
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(capitalizeWords('hello world'), 'Hello World')
	assert.deepStrictEqual(capitalizeWords('How are you doing, this...  lovely day?'), 'How Are You Doing, This...  Lovely Day?')
})();