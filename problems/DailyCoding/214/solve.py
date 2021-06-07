def solve(n: int) -> int:
	rep = bin(n)[2:]

	most = 0
	current = 0
	for i in rep:
		if i == '1':
			current += 1
		else:
			most = max(most, current)
			current = 0
	return max(most, current)


def test_solve():
	assert solve(156) == 3
	assert solve(1) == 1
	assert solve(3) == 2
	assert solve(7) == 3
	assert solve(15) == 4
	assert solve(31) == 5
	assert solve(63) == 6
