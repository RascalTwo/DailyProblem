
/**
 * @param {any[]} array
 * @param {number[]} indexes
 * @returns {any[]}
 */
function pickByIndexes(array, indexes){
	return indexes.map(index => array[index]);
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(pickByIndexes(['a', 'b', 'c'], [2, 1, 0]), ['c', 'b', 'a']);
	assert.deepStrictEqual(pickByIndexes(['d', 'a', 'c', 'b'], [1, 3, 2, 0]), ['a', 'b', 'c', 'd']);
})();