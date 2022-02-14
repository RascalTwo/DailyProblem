function solveIter(strings: string[]){
	const seen: Set<Set<string>> = new Set([new Set()]);
	for (const string of strings){
		const setStr = new Set(string);
		if (setStr.size == string.length){
			const newCombos: Set<Set<string>> = new Set();
			for (const combo of seen){
				if ([...setStr].every(char => !combo.has(char))){
					newCombos.add(new Set([...setStr, ...combo]))
				}
			}
			for (const combo of newCombos){
				seen.add(combo)
			}
		}
	}
	return [...seen].reduce((longest, combo) => {
		return combo.size > longest ? combo.size : longest;
	}, 0)
}


function recur(strings: Set<Set<string>>, current: Set<string>, cache: Record<string, number>){
	const cacheKey = [...current].sort().join('');
	if (cacheKey in cache) return cache[cacheKey]

	let best = current.size
	for (const string of strings){
		if ([...string].every(char => !current.has(char))){
			const copy = new Set(strings)
			copy.delete(string)
			const result = recur(copy, new Set([...current, ...string]), cache)
			if (result > best) best = result;
		}
	}
	cache[cacheKey] = best;

	return best;
}

function solveRecur(strings: string[]){
	const setStrings = new Set(strings
		.map(string => [string, new Set(string)] as [string, Set<string>])
		.filter(([string, set]) => string.length === set.size)
		.map(([_, set]) => set))
	return recur(setStrings, new Set(), {})
}


(() => {
	const assert = require('assert');

	for (const solve of [solveIter, solveRecur]){
		assert.deepStrictEqual(solve(['un', 'iq', 'ue']), 4);
		assert.deepStrictEqual(solve(['cha', 'r', 'act', 'ers']), 6);
		assert.deepStrictEqual(solve(['abcdefghijklmnopqrstuvwxyz']), 26);
		assert.deepStrictEqual(solve(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']), 16);
	}
})();
