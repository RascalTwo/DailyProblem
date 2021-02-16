from typing import Dict, List, Set



def solve(relation_map: Dict[str, List[str]]) -> List[Set[str]]:
	groups: List[Set[str]] = []

	for person, friends in relation_map.items():
		found = False
		for group in groups:
			if person in group:
				group |= set(friends)
				found = True

		if not found:
			groups.append(set([person, *friends]))

	return groups


def test_solve():
	assert sorted(solve({
		'Jack': ['Henry', 'Bob'],
		'Henry': ['Jack', 'Mike'],
		'Bob': ['Jack'],
		'Sally': ['Lindsey'],
		'Ashley': [],
		'Mike': ['Henry'],
		'Lindsey': []
	})) == sorted([{'Jack', 'Henry', 'Bob', 'Mike'}, {'Sally', 'Lindsey'}, {'Ashley'}])
