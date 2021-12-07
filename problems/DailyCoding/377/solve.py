import statistics

from typing import Iterable



def solve(k: int, *arr: int) -> Iterable[float]:
	for i in range(len(arr) - k + 1):
		yield statistics.median(arr[i:i + k])


def test_solve():
	assert list(solve(3, -1, 5, 13, 8, 2, 3, 3, 1)) == [5, 8, 8, 3, 3, 3]
