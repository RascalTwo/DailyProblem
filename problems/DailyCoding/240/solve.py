import random

from typing import List, Optional



def solve(positions: List[int]) -> int:
	swaps = 0

	for i in range(0, len(positions), 2):
		current = positions[i]
		j = i + 1
		neighbor = positions[j]
		if current == neighbor:
			continue

		k = next(k for k in range(j + 1, len(positions)) if positions[k] == current)
		positions[j], positions[k] = positions[k], positions[j]
		swaps += 1

	return swaps


def test_solve():

	def generate_random_pairs(n: int) -> List[int]:
		positions: List[int] = []
		for i in range(n):
			positions.extend([i, i])
		random.shuffle(positions)
		return positions

	def assert_solve(positions: List[int], expected_swaps: Optional[int] = None):
		swaps = solve(positions)

		if expected_swaps is not None:
			assert swaps == expected_swaps

		for i in range(0, len(positions), 2):
			assert positions[i] == positions[i + 1]

	assert_solve([1, 3, 2, 1, 3, 2], 2)
	assert_solve([1, 1, 2, 2, 3, 3], 0)
	assert_solve(generate_random_pairs(10))
