import itertools

from typing import List


def solve(integers: List[int]) -> bool:
	for a, b, c in itertools.permutations(integers, 3):
		if (a**2) + (b**2) == c**2:
			return True
	return False


def test_solve():
	assert solve([4, 12, 13, 7, 15, 17, 3, 4, 5]) is True
	assert solve([1, 2, 3]) is False
