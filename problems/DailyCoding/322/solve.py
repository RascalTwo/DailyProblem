def solve(n: int) -> int:
	result = 0

	while True:
		possible = sum(range(result + 1))
		if possible >= n and not (possible - n) & 1:
			break
		result += 1

	return result


def test_solve():
	assert solve(1) == 1
	assert solve(2) == 3
	assert solve(5) == 5
	assert solve(10) == 4
	assert solve(115) == 17
