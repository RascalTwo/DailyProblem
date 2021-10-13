/**
 * @param {number[]} listeners
 * @param {number[]} towers
 */
function bruteMinimumRange(listeners, towers){
	let distance = 1;
	while (true){
		const receiving = new Array(listeners.length).fill(false);
		for (const tower of towers){
			const [towerLeft, towerRight] = [tower - distance, tower + distance]
			for (const [i, listener] of listeners.entries()){
				if (listener >= towerLeft && listener <= towerRight) receiving[i] = true;
			}

			if (receiving.every(Boolean)) return distance;
		}
		distance++;
	}
}

/**
 * @param {number[]} listeners
 * @param {number[]} towers
 */
function calculateMinimumRange(listeners, towers){
	let longestDistance = Number.MIN_SAFE_INTEGER;
	for (const listener of listeners){
		let shortestDistance = Number.MAX_SAFE_INTEGER;
		for (const tower of towers){
			const distance = Math.abs(listener - tower)
			if (distance < shortestDistance) shortestDistance = distance;
		}
		if (shortestDistance > longestDistance) longestDistance = shortestDistance;
	}
	return longestDistance;
}

(() => {
	const assert = require('assert');

	for (const solve of [calculateMinimumRange, bruteMinimumRange]){
		assert.deepStrictEqual(solve([1, 5, 11, 20], [4, 8, 15]), 5);
	}
})();
