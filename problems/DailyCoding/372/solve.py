import math



def solve(number: int):
	if not number:
		return 1
	return int(math.log10(number if number > 0 else -number) + 1)


def test_solve():
	assert solve(1) == 1
	assert solve(9) == 1
	assert solve(10) == 2
	assert solve(0) == 1
	assert solve(-10) == 2
	assert solve(-99) == 2
	assert solve(100) == 3
	assert solve(150) == 3
