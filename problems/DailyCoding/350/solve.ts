function* generatePerfectSquares(max: number){
	let i = 1;
	while(true){
		const square = i * i;
		if (square > max) return;
		yield square;
		i++;
	}
}

/*
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
*/

function* combinationsWithReplacements<T>(values: T[], count: number){
	const indices = new Array(count).fill(0);
	yield indices.map(i => values[i]);
	while(true){
		let found = false;
		let i = count - 1;
		for (; i >= 0; i--){
			if (indices[i] != values.length - 1) {
				found = true;
				break
			}
		}
		if (!found) return;

		indices.splice(i, indices.length, ...new Array(count - i).fill(null).map(() => indices[i] + 1));
		yield indices.map(i => values[i]);
	}
}

function* solve(n: number){
	const squares = Array.from(generatePerfectSquares(n));
	for (let count = 1; count < squares.length; count++){
		for (let combo of combinationsWithReplacements(squares, count)){
			if (combo.reduce((total, value) => total + value) === n){
				yield combo.sort((a, b) => b - a);
			}
		}
	}
}


(() => {
	const assert = require('assert');

	const assertMatches = (input: number, expected: number[][]) => {
		assert.deepStrictEqual(JSON.stringify(Array.from(solve(input))), JSON.stringify(expected))
	}

	assertMatches(4, [[4]]);
	assertMatches(16, [[16]]);
	assertMatches(17, [[16, 1], [9, 4, 4]]);
	assertMatches(18, [[9, 9], [16, 1, 1]]);
	assertMatches(25, [[25], [16, 9], [16, 4, 4, 1]]);
})();
