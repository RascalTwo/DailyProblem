import statistics


from typing import Iterable



def solve(sequence: Iterable[int]) -> Iterable[float]:
	current = []
	for num in sequence:
		current.append(num)
		yield statistics.median(current)


def test_solve():
	assert list(solve([2, 1, 5, 7, 2, 0, 5])) == [2, 1.5, 2, 3.5, 2, 2, 2]
