from typing import Any, List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def height(node: Optional[Node]) -> int:
	return 0 if not node else 1 + max(height(node) for node in (node.left, node.right))


def is_height_balanced(node: Optional[Node]) -> bool:
	if not node:
		return True
	return abs(height(node.left) - height(node.right)) <= 1


def solve(array: List[int]) -> Optional[Node]:
	length = len(array)
	if length <= 1:
		return Node(array[0]) if length else None

	middle = length // 2
	return Node(array[middle], solve(array[:middle]), solve(array[middle + 1:]))


def test_solve():
	assert is_height_balanced(solve([1, 2, 3, 4, 5, 6, 7, 8, 9])) is True
	assert is_height_balanced(solve([1, 2, 3, 4, 5, 6, 7, 8])) is True
