def solve(n: int) -> int:
	perfect = 0

	for _ in range(n):
		perfect += 1
		while sum(map(int, str(perfect))) != 10:
			perfect += 1

	return perfect


def test_solve():
	assert solve(1) == 19
	assert solve(2) == 28
	assert solve(3) == 37
	assert solve(9) == 91
	assert solve(10) == 109
	assert solve(11) == 118
