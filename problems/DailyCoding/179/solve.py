from typing import Any, List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, o: Any) -> bool:
		return isinstance(o, Node) and self.value == o.value and self.left == o.left and self.right == o.right


def solve(postorder: List[int]) -> Optional[Node]:
	if not postorder:
		return None

	sides: List[List[int]] = [[], []]
	root = postorder[-1]
	for value in postorder[:-1]:
		sides[int(value > root)].append(value)

	return Node(root, solve(sides[0]), solve(sides[1]))


def test_solve():
	assert solve([2, 4, 3, 8, 7, 5]) == Node(5, Node(3, Node(2), Node(4)), Node(7, None, Node(8)))
