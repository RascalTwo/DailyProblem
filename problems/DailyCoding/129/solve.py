import math



def solve(n: int) -> float:
	return math.sqrt(n)


def test_solve():
	assert solve(9) == 3
