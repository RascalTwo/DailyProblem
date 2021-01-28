from typing import List



def solve(integers: List[int]) -> List[int]:
	i = 0
	while i < len(integers) - 1:
		a, b = integers[i:i + 2]
		if a == b:
			integers.pop(i + 1)
		else:
			i += 1

	return integers


def test_solve():
	assert solve([1, 1, 2]) == [1, 2]
	assert solve([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]
	assert solve([4, 4, 5, 7, 7, 7, 7, 8, 9, 10, 10, 10]) == [4, 5, 7, 8, 9, 10]
