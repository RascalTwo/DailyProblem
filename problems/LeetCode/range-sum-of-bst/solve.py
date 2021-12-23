from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node, min: int, max: int) -> int:
	return (root.value if min <= root.value <= max else 0) + sum(solve(child, min, max) for child in (root.left, root.right) if child)


def test_solve():
	assert solve(Node(5,
		Node(3, Node(2), Node(4)),
		Node(8, Node(6), Node(10))
	), 4, 9) == 23
	assert solve(Node(5,
		Node(3, Node(2), Node(4)),
		Node(8, Node(6), Node(10))
	), 5, 5) == 5
