from typing import Any, Optional, Tuple



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Node):
			return False
		return self.value == other.value and self.left == other.left and self.right == other.right


def solve(root: Node, k: int) -> Optional[Tuple[Node, Node]]:
	nodes = [root]
	searching = [root.right, root.left]
	while searching:
		node = searching.pop()
		while node:
			nodes.append(node)
			searching.append(node.right)
			node = node.left

	for i in range(len(nodes)):
		for j in range(i + 1, len(nodes)):
			if nodes[i].value + nodes[j].value == k:
				return nodes[i], nodes[j]

	return None


def test_solve():
	tree = Node(10, Node(15, Node(15), Node(11)), Node(5))
	assert solve(tree, 20) == (tree.left, tree.right)
