from typing import List


def solve(array: List[int]) -> List[int]:
	ranks = sorted(array)
	for i in range(len(array)):
		array[i] = ranks.index(array[i]) + 1
	return array


def test_solve():
	assert solve([0, 7, 3, 9]) == [1, 3, 2, 4]
	assert solve([3, 2]) == [2, 1]
