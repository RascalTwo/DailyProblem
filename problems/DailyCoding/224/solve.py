import itertools


from typing import List, Set



def solve(numbers: List[int]) -> int:
	sums: Set[int] = set()
	for size in range(1, len(numbers) + 1):
		sums |= set(sum(subset) for subset in itertools.combinations(numbers, size))

	for n in range(1, max(sums) + 1):
		if n not in sums:
			return n



def test_solve():
	assert solve([1, 2, 3, 10]) == 7
