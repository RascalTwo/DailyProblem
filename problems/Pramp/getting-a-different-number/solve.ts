function solveHashed(arr: number[]): number {
  const seen = new Set(arr);

  let result = 0;
  while(seen.has(result)) result++

  return result;
}


function solveSorted(arr: number[]): number {
  const sorted = arr.slice().sort();

	for (let i = 0; i < sorted.length; i++){
		if (sorted[i] !== i) return i;
  }

  return sorted.length;
}


function solveEfficientSorted(arr: number[]): number {
  for (let i = 0; i < arr.length; i++){
    let value = arr[i];
    while(value < arr.length && arr[value] != value){
      const temp = arr[value];
      arr[value] = value;
      value = temp;
    }
  }

  for (let i = 0; i < arr.length; i++){
    if (arr[i] !== i) return i;
  }

  return arr.length;
}

(() => {
	const assert = require('assert');

	for (const solve of [solveHashed, solveSorted, solveEfficientSorted]){
		assert.deepStrictEqual(solve([0]), 1);
		assert.deepStrictEqual(solve([0, 1, 2]), 3);
		assert.deepStrictEqual(solve([1, 3, 0, 2]), 4);
		assert.deepStrictEqual(solve([1000000]), 0);
		assert.deepStrictEqual(solve([1, 0, 3, 4, 5]), 2);
		assert.deepStrictEqual(solve([0, 1000000]), 1);
		assert.deepStrictEqual(solve([0, 99999, 1000000]), 1);
		assert.deepStrictEqual(solve([0, 5, 4, 1, 3, 6, 2]), 7);
	}
})();