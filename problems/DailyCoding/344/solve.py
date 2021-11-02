import itertools

from typing import Dict, List, Optional, Set, Tuple



class Node:
	def __init__(self, value: int, *children: 'Node'):
		self.value = value
		self.children = list(children)


def solve(root: Node) -> int:
	graph: Dict[int, List[int]] = {}

	stack = [root]
	while stack:
		current = stack.pop()
		destionations = graph.setdefault(current.value, [])
		for child in current.children:
			destionations.append(child.value)
			stack.append(child)

	values: Set[int] = set(graph.keys()) | set(value for valueset in graph.values() for value in valueset)

	edges: List[Tuple[int, int]] = []
	for source, dests in graph.items():
		for dest in dests:
			edges.append((source, dest))

	for keep_count in range(len(edges) - 1, -1, -1):
		for keeping_edges in itertools.combinations(edges, r=keep_count):
			attempt_graph: Dict[int, List[int]] = {}
			for source, dest in keeping_edges:
				attempt_graph.setdefault(source, []).append(dest)

			groups: List[Set[int]] = []
			for node in values:
				current_group: Optional[Set[int]] = next((members for members in groups if node in members), None)
				if current_group is None:
					current_group = set()
					groups.append(current_group)

				current_group.add(node)
				for dest in attempt_graph.get(node, []):
					current_group.add(dest)

			if all(len(members) % 2 == 0 for members in groups):
				return len(edges) - keep_count

	return 0


def test_solve():
	assert solve(Node(1,
		Node(2),
		Node(3, Node(4, Node(6), Node(7), Node(8)), Node(5))
	)) == 1
