from typing import Any, Dict, List, Optional, Set



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


	def __hash__(self):
		return hash(self.value) + hash(self.left) + hash(self.right)


def pathfind(graph: Dict[Node, Set[Node]], start: Node, end: Node, seen: Set[Node]) -> List[Node]:
	if start == end:
		return [start]

	for dest in graph[start]:
		if dest in seen:
			continue
		path = pathfind(graph, dest, end, seen | {start})
		if path and path[-1] == end:
			return [start, *path]

	return []



def solve(root: Node) -> List[Node]:
	graph: Dict[Node, Set[Node]] = {}
	processing = [root]
	while processing:
		node = processing.pop()
		graph.setdefault(node, set())
		for child in (node.left, node.right):
			if child:
				processing.append(child)
				graph[node].add(child)
				graph.setdefault(child, set()).add(node)


	best = []
	for start in graph.keys():
		for end in graph.keys():
			if start == end:
				continue
			path = pathfind(graph, start, end, {start})
			if path and (not best or sum(node.value for node in path) > sum(node.value for node in best)):
				best = path
	return best


def test_solve():
	assert solve(Node(1, Node(2), Node(3))) == [Node(2), Node(1, Node(2), Node(3)), Node(3)]
	assert solve(Node(-10, Node(9), Node(20, Node(15), Node(7)))) == [Node(15), Node(20, Node(15), Node(7)), Node(7)]
