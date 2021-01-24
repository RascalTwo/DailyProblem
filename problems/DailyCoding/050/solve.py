import operator


from typing import Generic, Optional, TypeVar, Union



T = TypeVar('T')


class Node(Generic[T]):
	def __init__(self, value: T, left: Optional['Node[T]'] = None, right: Optional['Node[T]'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(node: Node[Union[str, int]]) -> int:
	if isinstance(node.value, int):
		return node.value

	return getattr(operator, {'+': 'add', '-': 'sub', '*': 'mul', '/': 'truediv'}[node.value])(solve(node.left), solve(node.right))


def test_solve():
	assert solve(Node('*', Node('+', Node(5), Node(4)), Node('+', Node(3), Node(2)))) == 45
