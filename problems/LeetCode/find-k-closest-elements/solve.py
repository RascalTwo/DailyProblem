from typing import List



def solve(arr: List[int], k: int, x: int):
	return [
		arr[i]
		for i in sorted(
			sorted(
				range(len(arr)),
				key=lambda i: (abs(arr[i] - x), i)
			)[:k]
		)
	]


def test_solve():
	assert solve([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
	assert solve([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
	assert solve([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4) == [0, 1, 1, 1, 2, 3, 6, 7, 8]