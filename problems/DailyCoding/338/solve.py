def solve(n: int) -> int:
	count = bin(n).count('1')

	result = n + 1
	while  bin(result).count('1') != count:
		result += 1

	return result


def test_solve():
	assert solve(6) == 9
