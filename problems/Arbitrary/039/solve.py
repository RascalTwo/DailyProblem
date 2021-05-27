from typing import List, Set



def solve(steps: List[int]) -> bool:
	i = 0
	seen: Set[int] = set()
	while i not in seen and i != len(steps) - 1:
		seen.add(i)
		i += steps[i]
	return i == len(steps) - 1


def test_solve():
	assert solve([2, 3, 1, -2, 0]) is True
	# Positions: 0 -> 2 -> 3 -> 1 -> 4
	assert solve([1, 3, 1, 2, 0, 1]) is False
	assert solve([1, 2, 1, 0, 0]) is False
	assert solve([3, 1, 2, -2, 0]) is True
	assert solve([2, 2, -1, -3, 0]) is False
