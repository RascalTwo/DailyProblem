from typing import List



def solve(array: List[int]):
	return sum(array) - sum(range(len(array)))


def test_solve():
	assert solve([1, 2, 3, 4, 4, 5]) == 4
	assert solve([1, 2, 3, 3]) == 3
