
from typing import List



def solve(integers: List[int], k: int) -> int:
	best = 0

	if k == 0:
		count = 0
		for num in integers:
			if num == 1:
				count += 1
			else:
				best = max(best, count)
				count = 0
		return max(best, count)

	for i, num in enumerate(integers):
		if num == 1:
			continue
		integers[i] = 1
		best = max(best, solve(integers, k - 1))
		integers[i] = 0

	return best



def test_solve():
	assert solve([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
	assert solve([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 3) == 10

