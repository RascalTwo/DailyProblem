from typing import Optional


class Node:
	def __init__(self, value: int, left: Optional['Node'], right: Optional['Node']):
		self.value = value
		self.left = left
		self.right = right


def is_bst(root: Node) -> bool:
	return (
		(True if root.left is None else (root.left.value <= root.value and is_bst(root.left)))
		and
		(True if root.right is None else (root.right.value >= root.value and is_bst(root.right)))
	)


def solve(root: Node) -> int:
	left_size = 0 if root.left is None else solve(root.left)
	right_size = 0 if root.right is None else solve(root.right)
	if is_bst(root):
		return left_size + right_size + 1
	else:
		return max(left_size, right_size)


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
	)) == 7
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
	)) == 3
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
	)) == 3
