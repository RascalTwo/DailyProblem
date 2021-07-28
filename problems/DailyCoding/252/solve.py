from typing import Iterable



def solve(a: int, b: int) -> Iterable[int]:
	goal = a / b
	value = 0

	denominator = 1
	while value < goal:
		denominator += 1
		old_value = value
		value += 1 / denominator
		if value > goal:
			value = old_value
		else:
			yield denominator


def test_solve():
	assert list(solve(5, 8)) == [2, 8]
	assert list(solve(13, 12)) == [2, 3, 4]
	assert list(solve(4, 13)) == [4, 18, 468]
