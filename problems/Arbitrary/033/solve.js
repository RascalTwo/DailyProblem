/**
 * Return if the target word can be spelled using the characters in the words of phrase,
 * using at most one character from each word
 *
 * @param {string} target
 * @param {strin} phrase
 *
 * @returns {boolean}
 */
function canSpell(target, phrase){
	let found = 0;
	for (const word of phrase.split(' ')){
		if (!word.includes(target[found])) continue;

		found++;
		if (found == target.length) return true;
	}

	return found == target.length;
}


(() => {
	const assert = require('assert');

	// "boom" is within "everybody's looking for something" via "every[b]ody's l[o]oking f[o]r so[m]ething"
	assert.deepStrictEqual(canSpell('boom', 'everybody\'s looking for something'), true);
	assert.deepStrictEqual(canSpell('abc', 'everybody\'s looking for something'), false);
	assert.deepStrictEqual(canSpell('toe', 'It\'s the eye of the tiger'), true);
})();
