import functools


@functools.lru_cache(maxsize=None)
def solve(n: int) -> int:
	squares = n  # 1*1+1*1...

	for i in range(1, n // 2):
		if (squared := i * i) > n:
			break
		squares = min(squares, 1 + solve(n - squared))

	return squares


def test_solve():
	assert solve(13) == 2
	assert solve(27) == 3
