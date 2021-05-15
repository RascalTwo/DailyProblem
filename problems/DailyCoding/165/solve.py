from typing import List



def solve(integers: List[int]) -> List[int]:
	return [sum(1 for other in integers[i:] if other < num) for i, num in enumerate(integers)]


def test_solve():
	assert solve([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
	assert solve([1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]
	assert solve([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
