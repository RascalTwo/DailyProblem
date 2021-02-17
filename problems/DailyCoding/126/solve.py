from typing import Any, List



def solve(values: List[Any], k: int) -> List[Any]:
	return values[k:] + values[:k]


def test_solve():
	assert solve([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
	assert solve([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6]
	assert solve([1, 2, 3, 4, 5, 6], -2) == [5, 6, 1, 2, 3, 4]
	assert solve([1, 2, 3, 4, 5, 6], 6) == [1, 2, 3, 4, 5, 6]
