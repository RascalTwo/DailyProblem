from typing import Union



def solve(*integers: Union[int, float]) -> bool:
	if len(integers) <= 2:
		return True

	diff = abs(integers[0] - integers[1])
	return all(abs(value - integers[i + 2]) == diff for i, value in enumerate(integers[1:-1]))


def test_solve():
	assert solve() is True
	assert solve(1) is True
	assert solve(1, 2, 3) is True
	assert solve(-1, -2, -3) is True
	assert solve(-1, 0, 1) is True
	assert solve(0, 2, 4, 6, 8, 10) is True
	assert solve(0, 1.5, 3, 4.5, 6) is True
	assert solve(1, 2, 3, 2, 1) is True
	assert solve(1, 3, 2) is False
	assert solve(2, 1, 3) is False
