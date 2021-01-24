from typing import List



def solve(integers: List[int], k: int) -> List[int]:
	return [max(integers[i: i+k]) for i in range(len(integers) - k + 1)]


def test_solve():
	assert solve([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
