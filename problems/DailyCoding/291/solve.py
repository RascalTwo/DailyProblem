from typing import List


def solve(weights: List[int], limit: int) -> int:
	weights.sort()

	boats = 0
	while len(weights) > 1:
		r = len(weights) - 1
		while r:
			largest = weights[r]
			if largest == limit:
				boats += 1
				weights.pop(r)
				break

			if weights[0] + largest > limit:
				r -= 1
				continue

			boats += 1
			weights.pop(r)
			weights.pop(0)
			break

	return boats + len(weights)


def test_solve():
	assert solve([100, 200, 150, 80], 200) == 3
