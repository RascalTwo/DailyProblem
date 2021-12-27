from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value

		if left:
			left.parent = self
		self.left = left

		if right:
			right.parent = self
		self.right = right

		self.parent: Optional['Node'] = None


def solve(root: Node) -> Optional['Node']:
	current = root.parent
	while current:
		pass

	return current


def test_solve():
	assert solve(Node(10, Node(5), Node(30, Node(22), Node(35)))) == None
