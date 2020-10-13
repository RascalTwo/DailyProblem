import itertools

from typing import List



def solve(numbers: List[int], k: int, length: int = 2) -> bool:
	return any(sum(combo) == k for combo in itertools.combinations(numbers, length))


def test_solve():
	assert solve([10, 15, 3, 7], 17)
	assert solve([9, 4, 3, 6], 39) is False
	assert solve([7, 3, 15, 10], 17)

