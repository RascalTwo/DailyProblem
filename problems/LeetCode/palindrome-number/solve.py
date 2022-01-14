from typing import List



def solve(integer: int) -> bool:
	if integer < 0:
		return False

	digits: List[int] = []

	while integer:
		integer, remaining = divmod(integer, 10)
		digits.append(remaining)

	return digits == digits[::-1]


def test_solve():
	assert solve(121) is True
	assert solve(888) is True
	assert solve(678) is False
	assert solve(-121) is False
