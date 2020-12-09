def solve(x: int, y: int) -> int:
	result = 1

	for _ in range(y):
		result *= x

	return result


def test_solve():
	assert solve(2, 10) == 1024
	assert solve(5, 2) == 25
