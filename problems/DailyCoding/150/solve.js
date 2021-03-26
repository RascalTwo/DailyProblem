/**
 * @typedef {[number, number]} Point
 */

/**
 * Given a list of points, and a center points, return the k nearest points in order distance
 *
 * @param {Point[]} points
 * @param {Point} center
 * @param {number} k
 */
function getNearestPoints(points, center, k){
	for (let i = 0; i < k + 1; i++){
		for (let j = 0; j < points.length - i - 1; j++){
			if (distance(center, points[j]) > distance(center, points[j + 1])){
				const temp = points[j];
				points[j] = points[j + 1];
				points[j + 1] = temp;
			}
		}
	}

	return points.slice(0, k);
}


/**
 * @param {Point} a
 * @param {Point} b
 * @returns {number}
 */
 const distance = ([x1, y1], [x2, y2]) => Math.abs(Math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2)))


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(getNearestPoints([[0, 0], [3, 1], [5, 4]], [1, 2], 1), [[0, 0]]);
	assert.deepStrictEqual(getNearestPoints([[5, 4], [0, 0], [3, 1]], [1, 2], 2), [[0, 0], [3, 1]]);
	assert.deepStrictEqual(getNearestPoints([[3, 1], [5, 4], [0, 0]], [1, 2], 3), [[0, 0], [3, 1], [5, 4]]);
})();
