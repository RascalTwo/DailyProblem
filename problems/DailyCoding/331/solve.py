import itertools

from typing import List, Sequence, Tuple



def solve(initial: str) -> List[int]:
	best: Tuple[int, Sequence[bool]] = (len(initial), [])
	for flips in itertools.product([True, False], repeat=len(initial)):
		attempt = ''
		for i, char in enumerate(initial):
			if char == 'x':
				attempt += {True: 'y', False: 'x'}[flips[i]]
			else:
				attempt += {True: 'x', False: 'y'}[flips[i]]

		ys = False
		for char in attempt:
			if char == 'x' and ys:
				break
			if char == 'y':
				ys = True
		else:
			count = sum(flips)

			if best[0] is None:
				best = (count, flips)
				continue

			if count < best[0]:
				best = (count, flips)

	return [i for i, flipped in enumerate(best[1]) if flipped]


def test_solve():
	assert solve('xyxxxyxyy') == [1, 5]
	assert solve('yyyyyyyyy') == []
	assert solve('yyyyyyyyx') == [8]
	assert solve('xxxxxyyyx') == [8]
	assert solve('xyxyxyxyxy') == [1, 3, 5, 7]
