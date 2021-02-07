/**
 * Perform XOR cipher on the plaintext using the key
 *
 * @param {string} plaintext
 * @param {string} key
 *
 * @returns {string}
 */
function xorCipher(plaintext, key){
	return Array(plaintext.length).fill()
		.map((_, i) => plaintext.charCodeAt(i) ^ key.charCodeAt(i % key.length))
		.map(code => String.fromCharCode(code)).join('')
}



(() => {
	const assert = require('assert');

	for (const [plaintext, key] of [['Hello, World!', 'mouse', ['abc123', 'universal']]]){
		const encoded = xorCipher(plaintext, key);
		assert.deepStrictEqual(xorCipher(encoded, key), plaintext)
	}
})();