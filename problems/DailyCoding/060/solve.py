import itertools

from typing import List, Optional, Tuple



def solve(multiset: List[int]) -> Optional[Tuple[List[int], List[int]]]:
	for first_size in range(1, len(multiset)):
		for permu in itertools.permutations(multiset, first_size):
			other = multiset[:]
			for num in permu:
				other.remove(num)
			if sum(permu) == sum(other):
				return list(permu), multiset


def test_solve():
	assert solve([15, 5, 20, 10, 35, 15, 10]) == ([20, 35], [15, 5, 20, 10, 35, 15, 10])
	assert solve([15, 5, 20, 10, 35]) is None
