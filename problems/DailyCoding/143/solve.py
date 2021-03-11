from typing import List



def solve(lst: List[int], x: int) -> List[int]:
	results: List[List[int]] = [[], [], []]

	for num in lst:
		results[0 if num < x else 1 if num == x else 2].append(num)

	return [item for sub in results for item in sub]


def test_solve():
	assert solve([9, 12, 3, 5, 14, 10, 10], 10) == [9, 3, 5, 10, 10, 12, 14]
