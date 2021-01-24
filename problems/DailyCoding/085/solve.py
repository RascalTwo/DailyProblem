def solve(x: int, y: int, b: int) -> int:
	return (x & ~b + 1) | (y & b - 1)


def test_solve():
	assert solve(7, 9, 1) == 7
	assert solve(7, 9, 0) == 9
