from typing import List



def solve(ways: List[int]) -> List[int]:
	denominations: List[int] = [1]

	for i, value in enumerate(ways[1:], 1):
		if not value:
			continue

		denominations.append(i)
		for j in range(len(ways) - 1, i - 1, -1):
			ways[j] -= ways[j - i]

	return denominations


def test_solve():
	assert solve([1, 0, 1, 1, 2]) == [1, 2, 3, 4]
