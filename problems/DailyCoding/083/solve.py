from typing import Optional



class Node:
	def __init__(self, value: str, left: Optional['Node'], right: Optional['Node']):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: 'Node') -> bool:
		return self.value == other.value and self.left == other.left and self.right == other.right


def solve(root: Optional[Node]) -> Optional[Node]:
	if not root:
		return None
	root.left, root.right = solve(root.right), solve(root.left)
	return root


def test_solve():
	assert solve(
		Node('a',
			Node('b',
				Node('d', None, None),
				Node('e', None, None)
			),
			Node('c',
				Node('f', None, None),
				None
			)
		)
	) == Node('a',
			Node('c',
				None,
				Node('f', None, None)
			),
			Node('b',
				Node('e', None, None),
				Node('d', None, None)
			)
		)
test_solve()