/**
 * @param {string} initialPositions
 * @returns {string}
 */
function simulateDominos(initialPositions){
	const positions = Array.from(initialPositions);
	/** @type {Record<number, Set<string>>} */
	let mutatingPositions = {};

	/** @type {(i: number, char: string) => void} */
	const appendMutation = (i, char) => {
		const target = i + (char === '\\' ? -1 : 1);
		if (0 <= target && target < positions.length && positions[target] === '|'){
			if (!(target in mutatingPositions)) mutatingPositions[target] = new Set();
			mutatingPositions[target].add(char);
		}
	}

	for (const [i, char] of positions.entries()){
		if ('\\/'.includes(char)) appendMutation(i, char);
	}

	while (Object.keys(mutatingPositions).length) {
		const copy = { ...mutatingPositions };
		mutatingPositions = {};
		for (const [i, forces] of Object.entries(copy)){
			if (['\\', '/'].every(char => forces.has(char)) || positions[i] !== '|') continue;

			const char = forces.values().next().value;
			positions[i] = char;
			appendMutation(Number(i), char);
		}
	}

	return positions.join('');
}

(() => {
	const assert = require('assert');

	assert.deepStrictEqual(simulateDominos(String.raw`|\|/||||\|`), String.raw`\\|///\\\|`);
	assert.deepStrictEqual(simulateDominos(String.raw`||/|||\|\|`), String.raw`||//|\\\\|`);
})();