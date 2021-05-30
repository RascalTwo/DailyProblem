from typing import Dict, List, Set



class Node:
	def __init__(self, label: int):
		self.label = label
		self.connections: Set[Node] = set()

	def connect_to(self, other: 'Node'):
		self.connections.add(other)


def solve(matrix: List[List[int]]):
	node_map: Dict[int, Node] = {}
	for r, row in enumerate(matrix):
		node = node_map.setdefault(r, Node(r))
		for c, col in enumerate(row):
			if not col or c == r:
				continue
			other = node_map.setdefault(c, Node(c))
			node.connections.add(other)
			other.connections.add(node)
	nodes = list(node_map.values())

	groups: List[Set[Node]] = []
	while nodes:
		node = nodes.pop()
		for group in groups:
			if not any(other in group for other in node.connections):
				group.add(node)
				break
		else:
			groups.append(set([node]))

	return len(groups) == 2



def test_solve():
	assert solve([
		[0, 1],
		[1, 0],
	]) is True
	assert solve([
		[0, 0, 1, 1],
		[0, 0, 1, 1],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
	]) is True
	assert solve([
		[0, 0, 1, 1],
		[1, 0, 1, 1],
		[1, 1, 0, 0],
		[1, 1, 0, 0],
	]) is False
	assert solve([
		[0, 0, 0, 1, 1, 1],
		[0, 0, 0, 1, 1, 1],
		[0, 0, 0, 1, 1, 1],
		[1, 1, 1, 0, 0, 0],
		[1, 1, 1, 0, 0, 0],
		[1, 1, 1, 0, 0, 0]
	]) is True
	assert solve([
		[0, 0, 0, 1, 1, 1],
		[0, 0, 0, 1, 1, 1],
		[0, 1, 0, 1, 1, 1],
		[1, 1, 1, 0, 0, 0],
		[1, 1, 1, 0, 0, 0],
		[1, 1, 1, 0, 0, 0]
	]) is False
