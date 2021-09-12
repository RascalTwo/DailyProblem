import itertools

from typing import Dict, List, Set



def solve(preferences: Dict[int, List[int]]) -> Set[int]:
	preference_sets: List[Set[int]] = []

	drinks: Set[int] = set()
	for customer_drinks in map(set, preferences.values()):
		preference_sets.append(customer_drinks)
		drinks |= customer_drinks

	for count in range(1, len(drinks)):
		for learning in map(set, itertools.permutations(drinks, count)):
			if all(cd & learning for cd in preference_sets):
				return learning

	return set()


def test_solve():
	assert solve({
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
	}) == {1, 5}
