/**
 * @param {number} number
 * @returns {boolean}
 */
function isPalindrome(number){
	if (number < 0) return false;
	const digits = [];
	while (number){
		const remaining = number % 10;
		digits.push(remaining);

		number = Math.floor(number / 10);
	}

	for (let i = 0; i < Math.floor(digits.length / 2); i++){
		if (digits[i] !== digits[digits.length - i - 1]) return false;
	}
	return true
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(isPalindrome(121), true);
	assert.deepStrictEqual(isPalindrome(888), true);
	assert.deepStrictEqual(isPalindrome(678), false);
	assert.deepStrictEqual(isPalindrome(-121), false);
})();
