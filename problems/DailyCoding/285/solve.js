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
 * @yields {number}
 */
function *bruteGetBuildingsWithSunsetView(heights){
  for (let i = 0; i < heights.length; i++){
    let valid = true;
    for (let j = i + 1; j < heights.length; j++){
      if (heights[j] >= heights[i]){
        valid = false;
        break;
      }
    }
    if (valid) yield i;
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

	for (const solve of [getBuildingsWithSunsetView, bruteGetBuildingsWithSunsetView, functionallyGetBuildingsWithSunsetView]){
		assert.deepStrictEqual(Array.from(solve([3, 7, 8, 3, 6, 1])).sort(), [5, 4, 2].sort());
		assert.deepStrictEqual(Array.from(solve([5, 4, 3, 10])), [3]);
	}
})();
