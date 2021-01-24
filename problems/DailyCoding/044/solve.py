from typing import Iterable, List, Tuple



def solve(array: List[int]) -> Iterable[Tuple[int, int]]:
	for i, a in enumerate(array):
		for b in array[i:]:
			if a > b:
				yield (a, b)


def test_solve():
	assert list(solve([1, 2, 3, 4, 5])) == []
	assert list(solve([2, 4, 1, 3, 5])) == [(2, 1), (4, 1), (4, 3)]
	assert list(solve([5, 4, 3, 2, 1])) == [(5, 4), (5, 3), (5, 2), (5, 1), (4, 3), (4, 2), (4, 1), (3, 2), (3, 1), (2, 1)]
