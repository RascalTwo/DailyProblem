import functools


@functools.lru_cache(maxsize=None)
def solve(n: int) -> int:
	return 1 if n <= 1 else sum(solve(i - 1) * solve(n - i) for i in range(1, n + 1))


def test_solve():
	assert solve(1) == 1
	assert solve(2) == 2
	assert solve(3) == 5
	assert solve(4) == 14
	assert solve(5) == 42
	assert solve(6) == 132
	assert solve(15) == 9694845
