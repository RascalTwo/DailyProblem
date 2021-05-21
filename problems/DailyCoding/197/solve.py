from typing import Any, List



def solve(array: List[Any], k: int):
	for _ in range(k):
		array.insert(0, array.pop())


def test_solve():
	def test_solve(array: List[Any], k: int, rotated: List[Any]):
		solve(array, k)
		assert array == rotated

	test_solve([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2])
	test_solve([1, 2], 1, [2, 1])
	test_solve([1, 2, 3], 3, [1, 2, 3])
