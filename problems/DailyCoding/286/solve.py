import collections

from typing import DefaultDict, Dict, Iterable, List, Tuple


def solve(buildings: List[Tuple[int, int, int]]) -> Iterable[Tuple[int, int]]:
	heights: DefaultDict[int, int] = collections.defaultdict(int)
	for left, right, height in buildings:
		for x in range(left, right + 1):
			heights[x] = max(heights[x], height)

	last = 0
	for x in range(0, max(heights)):
		height = heights[x]

		if height > last:
			yield x, height
		elif height < last:
			yield x-1, height

		last = height

	yield max(heights), 0


def test_solve():
	assert list(solve([(0, 15, 3), (4, 11, 5), (19, 23, 4)])) == [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]
