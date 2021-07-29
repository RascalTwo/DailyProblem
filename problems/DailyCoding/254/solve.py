from typing import Any, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def is_full(node: Optional[Node]) -> bool:
	return (
		False
		if not node else
		(node.left is None and node.right is None) or
		(is_full(node.left) and is_full(node.right))
	)


def find_full(node: Optional[Node]) -> Optional[Node]:
	return (
		None
		if not node else
		node if is_full(node) else
		find_full(node.left) or find_full(node.right)
	)


def solve(node: Node) -> Node:
	if is_full(node):
		return node

	node.left = find_full(node.left)
	node.right = find_full(node.right)
	return node


def test_solve():
	assert solve(Node(0, Node(1, Node(3, None, Node(5))), Node(2, None, Node(4, Node(6), Node(7))))) == Node(0, Node(5), Node(4, Node(6), Node(7)))
