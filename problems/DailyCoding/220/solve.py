from typing import List



def solve(coins: List[int]):
	values = [0, 0]
	current = 0
	while coins:
		values[current] += coins.pop(0 if coins[0] > coins[-1] else -1)
		current = (current + 1) % len(values)
	return values[0]


def test_solve():
	assert solve([1, 2, 3, 4, 5, 6]) == 12
	assert solve([5, 3, 1, 2, 4, 6]) == 12
	assert solve([6, 4, 2, 5, 1, 3]) == 15
