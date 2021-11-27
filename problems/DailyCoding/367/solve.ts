function* mergeIterators(...iterables: IterableIterator<number>[]): Generator<number, any, any>{
	const values: Record<string, [number, IterableIterator<number>]> = iterables.reduce((values, iterator, i) => ({
		...values,
		[i]: [iterator.next().value, iterator]
	}), {});

	while (Object.keys(values).length){
		const i = Object.entries(values).reduce(
			(leastIndex, [i, [value, iterable]]) => value < values[leastIndex][0] ? i : leastIndex, '0'
		);
		const current = values[i];
		yield current[0];

		const { value } = current[1].next();
		if (value === undefined) delete values[i];
		else current[0] = value;
	}
}


(() => {
	const assert = require('assert');

	assert.deepStrictEqual(Array.from(mergeIterators([5, 10, 15].values(), [3, 8, 9].values())), [3, 5, 8, 9, 10, 15]);
	assert.deepStrictEqual(Array.from(mergeIterators([5, 10, 15].values(), [3, 8, 9].values(), [0, 12].values())), [0, 3, 5, 8, 9, 10, 12, 15]);
})();
