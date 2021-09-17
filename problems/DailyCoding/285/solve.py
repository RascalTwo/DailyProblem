import sys

from typing import Iterable, List



def solve(heights: List[int]) -> Iterable[int]:
	building_count = len(heights)
	yield building_count - 1

	highest = -sys.maxsize
	for i, height in enumerate(heights[::-1][1:], 2):
		if height > highest:
			yield building_count - i

		highest = max(highest, height)


def test_solve():
	assert list(solve([3, 7, 8, 3, 6, 1])) == [5, 4, 2]
