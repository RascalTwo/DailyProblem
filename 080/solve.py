from typing import Optional, Tuple



class Node:
	def __init__(self, value: str, left: Optional['Node'], right: Optional['Node']):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node, depth: int = 0) -> Tuple[Node, int]:
	return sorted(filter(bool, [
		(root, depth),
		solve(root.left, depth + 1) if root.left else None,
		solve(root.right, depth + 1) if root.right else None
	]), key = lambda pair: pair[1], reverse = True)[0]


def test_solve():
	assert solve(Node('a', Node('b', None, Node('d', None, None)), Node('c', None, None)))[0].value == 'd'
