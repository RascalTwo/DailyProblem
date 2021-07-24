def solve(a: float, b: float) -> float:
	return sum((abs(a - b), a, b)) / 2


def test_solve():
	assert solve(1, 2) == 2
	assert solve(50, 10) == 50
