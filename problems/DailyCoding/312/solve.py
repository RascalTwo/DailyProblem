import functools

@functools.lru_cache(None)
def solve(n: int) -> int:
	if n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4

	return sum(solve(i) + solve(n-i) for i in range(1, n))


def test_solve():
	assert solve(2) == 2
	assert solve(4) == 14
	assert solve(5) == 42
