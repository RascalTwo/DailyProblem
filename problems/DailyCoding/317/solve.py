def solve(m: int, n: int) -> int:
	result = m
	for i in range(m + 1, n + 1):
		result &= i
	return result


def test_solve():
	assert solve(12, 15) == 12
