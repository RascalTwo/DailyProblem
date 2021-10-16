from typing import Any, List, Optional, Union



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def generate_cartesian_tree(values: List[Union[int, Node]]) -> Optional[Node]:
	if len(values) <= 1:
		if not values:
			return None
		return Node(values[0]) if isinstance(values[0], int) else values[0]

	left = values.pop(0)
	root = values.pop(0)
	right = values.pop(0) if values else None

	node = Node(root, generate_cartesian_tree([left]), generate_cartesian_tree([right]))
	return generate_cartesian_tree([node, *values])


def test_solve():
	assert generate_cartesian_tree([3, 2, 6, 1, 9]) == Node(1, Node(2, Node(3), Node(6)), Node(9))
