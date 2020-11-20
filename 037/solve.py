import itertools

from typing import List, Set



def solve(input: Set[int]) -> List[Set[int]]:
	power_set = [set()]

	for i in range(len(input) + 1):
		for permutation in itertools.permutations(input, r=i):
			if (permutation_set := set(permutation)) not in power_set:
				power_set.append(permutation_set)

	return power_set


def test_solve():
	assert solve({1, 2, 3}) == [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
