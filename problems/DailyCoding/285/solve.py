import sys

from typing import Iterable, List



def solve(heights: List[int]) -> Iterable[int]:
	yield heights[-1]
	highest = -sys.maxsize
	for height in heights[::-1][1:]:
		if height > highest:
			yield height
		highest = max(highest, height)


def test_solve():
	assert list(solve([3, 7, 8, 3, 6, 1])) == [1, 6, 8]
