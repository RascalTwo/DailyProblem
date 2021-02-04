from typing import List



def solve(integers: List[int]) -> int:
	return next((i for i, value in enumerate(integers) if i == value), -1)


def test_solve():
	assert solve([7, 8, 5, 2, 4, 9]) == 4
	assert solve([7, 8, 5, 2, 8, 9]) == -1
