import itertools



def solve(n: int) -> int:
	completed = 0
	for row in itertools.count(1):
		completed += row
		if completed == n:
			return row
		if completed > n:
			return row - 1


def test_solve():
	assert solve(5) == 2
	assert solve(6) == 3
	assert solve(8) == 3
	assert solve(100000000000000) == 14142135