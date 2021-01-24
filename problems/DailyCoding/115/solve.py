from typing import Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'], right: Optional['Node']):
		self.value = value
		self.left = left
		self.right = right


def solve(haystack: Node, needle: Node) -> bool:
	if haystack.value != needle.value:
		return False or any(solve(child, needle) for child in (haystack.left, haystack.right) if child)

	for children in ((haystack.left, needle.left), (haystack.right, needle.right)):
		nones = [child is None for child in children]

		if all(nones):
			continue

		if any(nones):
			return False

		if not solve(*children):
			return False

	return True


def test_solve():
	tree = Node(1,
		Node(2,
			Node(3, None, None),
			Node(4, None, None)
		),
		Node(5,
			Node(6, None, None),
			Node(7, None, None)
		)
	)
	assert tree.left
	assert solve(tree, tree.left) is True

	assert tree.right
	assert solve(tree.right, tree.left) is False
