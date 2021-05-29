from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Optional[Node]) -> int:
	if not root:
		return 0
	return 1 + solve(root.left) + solve(root.right)


def test_solve():
	assert solve(Node(1, Node(2), Node(3))) == 3
	assert solve(Node(1, Node(2, Node(4), Node(5)), Node(3))) == 5
