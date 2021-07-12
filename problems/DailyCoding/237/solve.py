from typing import Any



class Tree:
	def __init__(self, value: int, *children: 'Tree'):
		self.value = value
		self.children = list(children)


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Tree) and self.value == other.value and self.children == other.children


def solve(tree: Tree) -> bool:
	length = len(tree.children)
	if length <= 1:
		return True

	for i in range(length // 2):
		if tree.children[i] != tree.children[(length-1) - i]:
			return False
	return True


def test_solve():
	assert solve(Tree(4,
		Tree(3, Tree(9)),
		Tree(5),
		Tree(3, Tree(9))
	)) is True
	assert solve(Tree(4,
		Tree(3, Tree(9)),
		Tree(5),
		Tree(4, Tree(9))
	)) is False
	assert solve(Tree(4,
		Tree(3, Tree(9)),
		Tree(5),
		Tree(3, Tree(9), Tree(10))
	)) is False
