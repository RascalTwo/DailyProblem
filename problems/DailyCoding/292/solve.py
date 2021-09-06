from typing import Dict, List, Set, Tuple, Union


def solve(adjacency_list: Dict[int, List[int]]) -> Union[bool, Tuple[Set[int], Set[int]]]:
	nodes: Set[int] = set(adjacency_list.keys())

	completed: List[Set[int]] = []

	groups: List[Set[int]] = [set([key]) for key in adjacency_list.keys()]
	while groups:
		group = groups.pop()

		possibles = nodes - group
		for possible in possibles.copy():
			if any(member in adjacency_list[possible] for member in group):
				possibles.remove(possible)

		for possible in possibles:
			generated: Set[int] = set([*group, possible])
			if generated not in groups:
				groups.append(generated)

		if not possibles and group not in completed:
			completed.append(group)

	for i, first in enumerate(completed):
		for j in range(i, len(completed)):
			second = completed[j]
			if first.symmetric_difference(second) == nodes:
				return first, second
	return False


def test_solve():
	assert solve({
		0: [3],
		1: [2],
		2: [1, 4],
		3: [0, 4, 5],
		4: [2, 3],
		5: [3]
	}) == ({0, 1, 4, 5}, {2, 3})

	assert solve({
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
	}) is False
