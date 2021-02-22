function squareRoot(n){
	return Math.sqrt(n);
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(squareRoot(9), 3);
})();
