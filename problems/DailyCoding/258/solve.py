from typing import List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node) -> List[int]:
	output: List[int] = [root.value]
	ltr = True

	nodes: List[Optional[Node]] = []
	next_nodes: List[Optional[Node]] = [root.left, root.right]
	while nodes or next_nodes:
		if not nodes:
			nodes = next_nodes
			next_nodes = []
			ltr = not ltr

		node = nodes.pop()
		if not node:
			continue

		output.append(node.value)
		next_nodes.extend([node.left, node.right] if ltr else [node.right, node.left])

	return output


def test_solve():
	assert solve(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))) == [1, 3, 2, 4, 5, 6, 7]
