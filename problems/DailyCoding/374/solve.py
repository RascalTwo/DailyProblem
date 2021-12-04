from typing import List


def solve(arr: List[int]):
	for i, number in enumerate(arr):
		if i == number:
			return i


def test_solve():
	assert solve([-5, -3, 2, 3]) == 2
