from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def count_unival(root: Optional[Node]) -> int:
	return 0 if not root else is_unival(root) + count_unival(root.left) + count_unival(root.right)


def is_unival(root: Optional[Node]) -> bool:
	return not root or (
		(leaves := (root.left, root.right))
		and len(set((root.value, *(leaf.value for leaf in leaves if leaf)))) == 1
		and all(is_unival(leaf) for leaf in leaves)
	)


def test_solve():
	assert count_unival(
		Node(0,
			Node(1),
			Node(0,
				Node(1,
					Node(1),
					Node(1)
				),
				Node(0)
			)
		)
	) == 5
	assert count_unival(
		Node(0,
			Node(0),
			Node(0)
		)
	) == 3
	assert count_unival(
		Node(0,
			Node(1),
			Node(0)
		)
	) == 2
	assert count_unival(
		Node(0,
			Node(0,
				Node(0),
				None
			),
			Node(0)
		)
	) == 4
	assert count_unival(
		Node(0,
			Node(1,
				Node(0),
				None
			),
			Node(0)
		)
	) == 2
	assert count_unival(
		Node(0,
			Node(0,
				Node(1)
			)
		)
	) == 1
