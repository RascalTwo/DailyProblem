from typing import List



def solve(integers: List[int], k: int) -> List[int]:
	for i in range(len(integers)):
		total = 0
		for j in range(i, len(integers)):
			total += integers[j]
			if total == k:
				return integers[i:j+1]
			if total > k:
				break

	return []


def test_solve():
	assert solve([1, 2, 3, 4, 5], 9) == [2, 3, 4]
	assert solve([9, 4, 3, 6, 5, 1, 8], 14) == [3, 6, 5]
