from typing import List, Optional


def solve(S: List[int], k: int) -> Optional[List[int]]:
	for i, num in enumerate(S):
		remaining = k - num
		if not remaining:
			return [num]

		if found := solve(S[0:i] + S[i + 1:], remaining):
			return sorted([num] + found, reverse=True)

	return None


def test_solve():
	assert solve([12, 1, 61, 5, 9, 2], 24) == [12, 9, 2, 1]
