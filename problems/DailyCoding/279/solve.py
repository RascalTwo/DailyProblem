from typing import Dict, List, Set, TypeVar



T = TypeVar('T')

def solve(relation_map: Dict[T, List[T]]) -> List[Set[T]]:
	groups: List[Set[T]] = []

	for person, friends in relation_map.items():
		for group in groups:
			if person in group:
				group |= set(friends)
				break
		else:
			groups.append(set([person, *friends]))

	return groups


def test_solve():
	assert sorted(solve({
		0: [1, 2],
		1: [0, 5],
		2: [0],
		3: [6],
		4: [],
		5: [1],
		6: [3]
	})) == sorted([{0, 1, 2, 5}, {3, 6}, {4}])

	assert sorted(solve({
		'Jack': ['Henry', 'Bob'],
		'Henry': ['Jack', 'Mike'],
		'Bob': ['Jack'],
		'Sally': ['Lindsey'],
		'Ashley': [],
		'Mike': ['Henry'],
		'Lindsey': []
	})) == sorted([{'Jack', 'Henry', 'Bob', 'Mike'}, {'Sally', 'Lindsey'}, {'Ashley'}])
