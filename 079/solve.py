from typing import List



def solve(integers: List[int]) -> bool:
	changed = False
	for i in range(len(integers) - 1):
		if integers[i] > integers[i + 1]:
			if changed:
				return False
			changed = True

	return True


def test_solve():
	assert solve([10, 5, 7]) is True
	assert solve([10, 5, 1]) is False
	assert solve([0, 1, 2, 3, 4, 5]) is True
	assert solve([0, 1, 2, 9, 4, 5]) is True
	assert solve([0, 1, 2, 15, 12, 10]) is False
