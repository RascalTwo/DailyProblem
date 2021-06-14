from typing import List



def solve(coins: List[int]):
	values = [0, 0]
	current = 0
	while coins:
		values[current] += coins.pop()
		current = (current + 1) % len(values)
	return values[0]


def test_solve():
	assert solve([1, 2, 3, 4, 5, 6]) == 12
