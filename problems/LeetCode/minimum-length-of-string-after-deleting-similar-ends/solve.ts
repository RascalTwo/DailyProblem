function solve(target: string): number{
	while(true){
		const length = target.length;

		let prefix = 0
		let suffix = length - 1
		if (!length || prefix == suffix || target[prefix] != target[suffix]){
			return length
		}

		for (let i = 1; i < target.length; i++){
			if (target[i] === target[prefix] && i != suffix) prefix = i;
			else break;
		}

		for (let i = length - 2; i >= 0; i--){
			if (target[i] === target[suffix] && i != prefix) suffix = i;
			else break;
		}
		target = target.substring(prefix + 1, suffix);
	}
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve('ca'), 2);
	assert.deepStrictEqual(solve('cabaabac'), 0);
	assert.deepStrictEqual(solve('aabccabba'), 3);
	assert.deepStrictEqual(solve('bab'), 1);
	assert.deepStrictEqual(solve('a'), 1);
})();