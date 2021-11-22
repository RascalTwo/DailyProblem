function solve(jewels: string, stones: string){
	const jewelSet = new Set(jewels);

	let count = 0;
	for (const stone of stones){
			if (jewelSet.has(stone)) count++;
	}
	return count;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(solve('z', 'ZZ'), 0);
	assert.deepStrictEqual(solve('aA', 'aAAbbbb'), 3);
})();
