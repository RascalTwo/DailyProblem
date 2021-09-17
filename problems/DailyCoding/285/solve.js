/**
 * @param {number[]} heights
 * @yields {number}
 */
function* getBuildingsWithSunsetView(heights) {
  const count = heights.length;
  yield count - 1;

  let highest = Number.MIN_SAFE_INTEGER;
  for (const [offset, height] of heights.slice(0, -1).reverse().entries()) {
    if (height > highest) yield count - offset - 2;
    highest = Math.max(highest, height);
  }
}


/**
 * @param {number[]} heights
 * @yields {number}
 */
function* functionallyGetBuildingsWithSunsetView(heights) {
  yield * Array.from(heights.slice().reverse().entries()).reduce(
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
	}
})();
