from typing import Iterable



def solve(cents: int) -> Iterable[int]:
	denominations = [1, 5, 10, 25]
	while cents:
		denomination = denominations.pop()
		if denomination <= cents:
			yield from [denomination] * (cents // denomination)
			cents = cents % denomination


def test_solve():
	assert list(solve(16)) == [10, 5, 1]
	assert list(solve(93)) == [25, 25, 25, 10, 5, 1, 1, 1]
