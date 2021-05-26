from typing import List



def solve(integers: List[int]) -> int:
	length = len(integers)
	if length == 1:
		return integers[0]
	elif length == 2:
		return min(integers)

	middle = length // 2
	return min(
		solve(integers[:middle]),
		solve(integers[middle:])
	)


def test_solve():
	assert solve([5, 7, 10, 3, 4]) == 3
	assert solve([10, 11, 3, 4, 5, 7]) == 3
