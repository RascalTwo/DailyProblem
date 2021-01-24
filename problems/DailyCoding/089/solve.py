from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'], right: Optional['Node']):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node) -> bool:
	return (
		(True if root.left is None else (root.left.value <= root.value and solve(root.left)))
		and
		(True if root.right is None else (root.right.value >= root.value and solve(root.right)))
	)


def test_solve():
	assert solve(Node(0,
		Node(-2,
			Node(-3,
				None,
				Node(-1, None, None)
			),
			None
		),
		Node(2,
			Node(1,
				None,
				Node(3, None, None)
			),
			None
		)
	)) is True
	assert solve(Node(0,
		Node(-2,
			Node(-3,
				None,
				Node(-1, None, None)
			),
			None
		),
		Node(2,
			Node(1,
				None,
				Node(0, None, None)
			),
			None
		)
	)) is False
	assert solve(Node(0,
		Node(-2,
			Node(-3,
				None,
				Node(-1, None, None)
			),
			None
		),
		Node(2,
			Node(4,
				None,
				Node(3, None, None)
			),
			None
		)
	)) is False
