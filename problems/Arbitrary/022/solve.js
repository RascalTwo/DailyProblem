/**
 * Defang a URI
 *
 * @param {string} uri
 *
 * @returns {string}
 */
function defang(uri){
	return uri.replace(/\./g, '[.]');
}

/**
 * Refang a URI
 *
 * @param {string} uri
 *
 * @returns {string}
 */
function refang(uri){
	return uri.replace(/\[\.\]/g, '.');
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(defang('192.168.1.1'), '192[.]168[.]1[.]1');
	assert.deepStrictEqual(refang('192[.]168[.]1[.]1'), '192.168.1.1');

	assert.deepStrictEqual(defang('http://www.google.com/'), 'http://www[.]google[.]com/');
	assert.deepStrictEqual(refang('http://www[.]google[.]com/'), 'http://www.google.com/');
})();