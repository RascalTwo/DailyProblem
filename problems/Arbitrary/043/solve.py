from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(node: Optional[Node]) -> int:
	return 0 if not node else node.value + solve(node.left) + solve(node.right)


def test_solve():
	assert solve(Node(1,
		Node(2, Node(3)),
		Node(4, None, Node(5))
	)) == 15

	assert solve(Node(1,
		Node(2, Node(3)),
		Node(4, None, Node(-5))
	)) == 5