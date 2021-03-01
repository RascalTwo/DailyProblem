from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node) -> int:
	if not root.left and not root.right:
		return root.value

	return root.value + min(solve(child) for child in (root.left, root.right) if child)


def test_solve():
	assert solve(Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1))))) == 15
