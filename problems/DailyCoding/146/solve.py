from typing import Any, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		if not isinstance(self, Node):
			return False

		return self.value == other.value and self.left == other.left and self.right == other.right


def solve(node: Node) -> Optional[Node]:
	if node.left:
		node.left = solve(node.left)
	if node.right:
		node.right = solve(node.right)

	if not node.left and not node.right and not node.value:
		return None

	return node


def test_solve():
	assert solve(
		Node(0,
			Node(1),
			Node(0,
				Node(1,
					Node(0),
					Node(0)
				),
				Node(0)
			)
		)
	) == Node(0,
		Node(1),
		Node(0,
			Node(1)
		)
	)
