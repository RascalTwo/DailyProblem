from typing import Iterable, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(node: Optional['Node']) -> Iterable[int]:
	if not node:
		return []

	yield from solve(node.left)
	yield node.value
	yield from solve(node.right)


def test_solve():
	assert list(solve(Node(1, Node(2, Node(3), Node(4)), Node(5, Node(6), Node(7))))) == [3, 2, 4, 1, 6, 5, 7]
