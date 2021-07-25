import itertools

from typing import List



def solve(integers: List[int]) -> int:
	return max(pair[0] ^ pair[1] for pair in itertools.permutations(integers, 2))


def test_solve():
	assert solve([2, 2]) == 0
	assert solve([2, 4]) == 6
	assert solve([1, 2, 3, 4, 5]) == 7
