from typing import List



def solve(numbers: List[int]) -> int:
	return len(set(numbers))


def test_solve():
	assert solve([5, 1, 3, 5, 2, 3, 4, 1]) == 5
