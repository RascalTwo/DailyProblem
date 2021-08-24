from typing import Any, Iterable, Optional



class Node:
	def __init__(self, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.left == other.left and self.right == other.right


def solve(n: int) -> Iterable[Node]:
	if n == 1:
		yield Node()
		return

	for node in solve(n - 1):
		yield from [Node(node), Node(None, node)]


def test_solve():
	assert list(solve(1)) == [Node()]
	assert list(solve(2)) == [Node(Node()), Node(None, Node())]
	assert list(solve(3)) == [
		Node(Node(Node())),
		Node(None, Node(Node())),
		Node(Node(None, Node())),
		Node(None, Node(None, Node())),
	]