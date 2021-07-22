from typing import List



def solve(steps: List[int], index: int = 0) -> List[int]:
	if len(steps) == 1:
		return []

	possible = steps[0]
	if possible >= len(steps):
		return [index]
	least = steps[:]
	for distance in range(possible, 0, -1):
		d = solve(steps[distance:], index + distance)
		if len(least) > len(d):
			least = d
	return [index] + least


def test_solve():
	assert solve([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]) == [0, 4]
	assert solve([1, 1, 1, 1]) == [0, 1, 2]
	assert solve([9, 1, 1, 1]) == [0]
