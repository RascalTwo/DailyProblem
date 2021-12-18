from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node, target: int) -> bool:
	children = [child for child in (root.left, root.right) if child]
	return True if not children and root.value == target else any(solve(child, target - root.value) for child in children)


def test_solve():
	assert solve(Node(8, Node(4, Node(2), Node(6)), Node(13, Node(19))), 18) is True
	assert solve(Node(8, Node(4, Node(2), Node(6)), Node(13, Node(19))), 19) is False
	assert solve(Node(8, Node(4, Node(2), Node(6)), Node(13, Node(19))), 12) is False
