def solve(n: int, m: int, x: int = 1, y: int = 1) -> int:
	return (
		0 if x > n or y > m else 1
		if x >= n or y >= m else
		solve(n, m, x + 1, y) + solve(n, m, x, y + 1)
	)


def test_solve():
	assert solve(2, 2) == 2
	assert solve(5, 5) == 70
	assert solve(10, 10) == 48620
