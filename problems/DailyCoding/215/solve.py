from typing import Dict, List, Optional


class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node) -> List[int]:
	distances: Dict[int, int] = {}

	def recur(node: Optional[Node], offset: int):
		if not node:
			return

		distances[offset] = node.value
		recur(node.left, offset - 1)
		recur(node.right, offset + 1)

	recur(root, 0)

	return [value for _, value in sorted(distances.items(), key=lambda pair: pair[0])]


def test_solve():
	assert solve(Node(5,
		Node(3, Node(1, Node(0)), Node(4)),
		Node(7, Node(6), Node(9, Node(8)))
	)) in [[0, 1, 3, 6, 8, 9], [0, 1, 3, 4, 8, 9]]
