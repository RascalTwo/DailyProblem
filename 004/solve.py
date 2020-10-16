from typing import List



def solve(integers: List[int]) -> int:
	least = 0
	most = 0

	for number in integers:
		if number <= 0:
			continue

		if not least or (number < least):
			least = number

		if not most or (number > most):
			most = number

	return next(
		iter(set(range(least + 1, most)) - set(integers)),
		most + 1
	)


def test_solve():
	assert solve([3, 4, -1, 1]) == 2
	assert solve([2, 4, -1, 1]) == 3
	assert solve([1, 2, 0]) == 3
	assert solve([-1, -2, 0]) == 1
