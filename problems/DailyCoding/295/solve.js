function solveBrute(height){
	if (!height) return [];

	const rows = [{0: 1}]
	for (let _ = 0; _ < height; _++){
		const last = rows.slice(-1)[0];
		const indexes = Object.keys(last).map(Number);
		const start = Math.min(...indexes)
		const end = Math.max(...indexes)
		const row = {
			[start-1]: last[start],
			[end+1]: last[end]
		}
		for (let i = start + 1; i < end + 1; i += 2){
			row[i] = last[i - 1] + last[i + 1]
		}
		rows.push(row)
	}
	return Object.entries(rows.slice(-1)[0]).sort(([a], [b]) => a - b).map(([_, v]) => v)
}

function solveOptimized(height){
	if (!height) return [];

	let last = {0: 1}
	for (let _ = 0; _ < height; _++){
		const indexes = Object.keys(last).map(Number);
		const start = Math.min(...indexes)
		const end = Math.max(...indexes)
		const next = {
			[start-1]: last[start],
			[end+1]: last[end]
		}
		for (let i = start + 1; i < end + 1; i += 2){
			next[i] = last[i - 1] + last[i + 1]
		}
		last = next
	}
	return Object.entries(last).sort(([a], [b]) => a - b).map(([_, v]) => v)
}

(() => {
	const assert = require('assert');

	for (const solve of [solveBrute, solveOptimized]){
		assert.deepStrictEqual(solve(3), [1, 3, 3, 1]);
		assert.deepStrictEqual(solve(4), [1, 4, 6, 4, 1]);
	}
})();