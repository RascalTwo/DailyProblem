from typing import Any, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def merge_binary_trees(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
	if a is None:
		return b
	if b is None:
		return a
	return Node(a.value + b.value, merge_binary_trees(a.left, b.left), merge_binary_trees(a.right, b.right))


def test_solve():
	assert merge_binary_trees(Node(1, Node(2, Node(3), Node(4))), Node(1, Node(2, Node(3), Node(4)))) == Node(2, Node(4, Node(6), Node(8)))
	assert merge_binary_trees(Node(1, Node(2)), Node(1, None, Node(2))) == Node(2, Node(2), Node(2))
