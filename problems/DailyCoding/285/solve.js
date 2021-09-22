/**
 * @param {number[]} heights
 * @yields {number}
 */
function* getBuildingsWithSunsetView(heights) {
  const count = heights.length;

  let highest = 0;
  for (const [offset, height] of heights.slice().reverse().entries()) {
    if (height > highest) yield count - offset - 1;
    highest = Math.max(highest, height);
  }
}


/**
 * @param {number[]} heights
 * @returns {number[]}
 */
function functionallyGetBuildingsWithSunsetView(heights) {
  return Array.from(heights.slice().reverse().entries()).reduce(
    ({ sunsetViewing, highest: previousHighest }, [offset, height]) => ({
      highest: Math.max(previousHighest, height),
      sunsetViewing: height > previousHighest ? [...sunsetViewing, heights.length - offset - 1] : sunsetViewing,
    }),
    { sunsetViewing: [], highest: 0 },
  ).sunsetViewing;
}


(() => {
  const assert = require('assert');

	for (const solve of [getBuildingsWithSunsetView, functionallyGetBuildingsWithSunsetView]){
		assert.deepStrictEqual(Array.from(solve([3, 7, 8, 3, 6, 1])), [5, 4, 2]);
		assert.deepStrictEqual(Array.from(solve([5, 4, 3, 10])), [3]);
	}
})();
