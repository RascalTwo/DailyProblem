from typing import List


def solve(integers: List[int]):
	ints = set(integers)
	least = min(integers)
	most = max(integers) + 1

	best = set((integers[0], ))
	for i in range(least, most):
		for j in range(i + 1, most + 1):
			if (attempt := set(range(i, j))) & ints == attempt and len(attempt) > len(best):
				best = attempt
	return min(best), max(best)





def test_solve():
	assert solve([9, 6, 1, 3, 8, 10, 12, 11]) == (8, 12)
