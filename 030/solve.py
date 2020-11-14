from typing import List



def solve(elevations: List[int]) -> int:
	return (most := min(elevations[::len(elevations)])) and sum(
		diff
		for elevation in elevations[1:-1]
		if (diff := most - elevation) > 0
	)


def test_solve():
	assert solve([2, 1, 2]) == 1
	assert solve([3, 0, 1, 3, 0, 5]) == 8
	assert solve([3, 0, 1, 5, 0, 5]) == 8
