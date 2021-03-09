/**
 * Return the least valued coins to sum up to total
 *
 * @param {number} total
 *
 * @yields {number} coin value
 */
function* getCoins(denominations: number[], total: number){
	while(denominations.length){
		const denomination = denominations.pop()!;
		if (denomination <= total){
			// @ts-ignore
			yield* new Array(parseInt(total / denomination)).fill(denomination);
			total %= denomination;
		}
	}
	return null;
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual([...getCoins([1, 5, 10, 25], 16)], [10, 5, 1]);
	assert.deepStrictEqual([...getCoins([1, 5, 10, 25], 93)], [25, 25, 25, 10, 5, 1, 1, 1]);
})();

function countDynamic(denominations: Set<number>, target: number){
	const counts = new Array(target + 1).fill(0);
	for (let i = 1; i < target + 1; i++){
		counts[i] = Number.MAX_SAFE_INTEGER;
		for (const coin of denominations){
			if (i - coin >= 0){
				const result = counts[i - coin]
				if (result != Number.MAX_SAFE_INTEGER) {
					counts[i] = Math.min(counts[i], result + 1);
				}
			}
		}
	}
	return counts[target];
}

function countRecur(denominations: Set<number>, target: number){
	if (!target) return 0;
	if (target < 0) return Number.MAX_SAFE_INTEGER;

	let coins = Number.MAX_SAFE_INTEGER;
	for (const coin of denominations){
		const result = countRecur(denominations, target - coin);
		coins = Math.min(coins, result + 1);
	}

	return coins
}


function countIter(denominations: Set<number>, target: number){
	let best = Number.MAX_SAFE_INTEGER;
	const processing: [number, number][] = [[0, target]];
	while (processing.length){
		// @ts-ignore
		const [count, remaining] = processing.pop();
		if (remaining < 0) continue;
		if (!remaining) {
			best = Math.min(count, best);
			continue
		}
		for (const coin of denominations){
			processing.push([count + 1, remaining - coin]);
		}
	}

	return best
}


(() => {
	const assert = require('assert');
	for (const count of [countDynamic, countRecur, countIter]){
		assert.deepStrictEqual(count(new Set([5, 8]), 15), 3);
		assert.deepStrictEqual(count(new Set([5, 8, 10]), 15), 2);
		assert.deepStrictEqual(count(new Set([1, 5, 10]), 56), 7);
		assert.deepStrictEqual(count(new Set([1, 3, 5, 7]), 15), 3);
	}
})();
