from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def height(node: Optional[Node]) -> int:
	return 0 if not node else 1 + max(height(node) for node in (node.left, node.right))


def solve(node: Optional[Node]) -> bool:
	if not node:
		return True
	return solve(node.left) and solve(node.right) and abs(height(node.left) - height(node.right)) <= 1


def test_solve():
	assert solve(Node(0, Node(1, Node(2)))) is False
	assert solve(Node(0, Node(1))) is True
	assert solve(Node(0, Node(1), Node(2, Node(3)))) is True
	assert solve(Node(0, Node(1), Node(2, Node(3, Node(4))))) is False
