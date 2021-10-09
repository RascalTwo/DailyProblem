import functools
import math



@functools.lru_cache(None)
def solve(n: int) -> int:
	return 0 if n == 1 else 1 + solve(min((int(n / divisor) for divisor in range(2, int(math.sqrt(n)) + 1) if n % divisor == 0), default = n - 1))


def test_solve():
	assert solve(100) == 5
	assert solve(15) == 4
