from typing import List



def solve(integers: List[int]) -> int:
	return next((i for i, value in enumerate(integers) if i == value), -1)


def test_solve():
	assert solve([7, 8, 5, 2, 4, 9]) == 4
	assert solve([7, 8, 5, 2, 8, 9]) == -1
	assert solve([-6, 0, 2, 40]) == 2
	assert solve([1, 5, 7, 8]) == -1
