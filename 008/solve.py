from typing import Generic, Optional, TypeVar



T = TypeVar('T')


class Node(Generic[T]):
	def __init__(self, value: T, left: Optional['Node[T]'], right: Optional['Node[T]']):
		self.value = value
		self.left = left
		self.right = right


def count_unival(root: Optional[Node[T]]) -> int:
	return 0 if not root else is_unival(root) + count_unival(root.left) + count_unival(root.right)


def is_unival(root: Optional[Node[T]]) -> bool:
	return not root or (
		(leaves := (root.left, root.right))
		and len(set((root.value, *(leaf.value for leaf in leaves if leaf)))) == 1
		and all(is_unival(leaf) for leaf in leaves)
	)


def test_solve():
	assert count_unival(
		Node(0,
			Node(1, None, None),
			Node(0,
				Node(1,
					Node(1, None, None),
					Node(1, None, None)
				),
				Node(0, None, None)
			)
		)
	) == 5
	assert count_unival(
		Node(0,
			Node(0, None, None),
			Node(0, None, None)
		)
	) == 3
	assert count_unival(
		Node(0,
			Node(1, None, None),
			Node(0, None, None)
		)
	) == 2
	assert count_unival(
		Node(0,
			Node(0,
				Node(0, None, None),
				None
			),
			Node(0, None, None)
		)
	) == 4
	assert count_unival(
		Node(0,
			Node(1,
				Node(0, None, None),
				None
			),
			Node(0, None, None)
		)
	) == 2
	assert count_unival(
		Node(0,
			Node(0,
				Node(1, None, None),
				None
			),
			None
		)
	) == 1
