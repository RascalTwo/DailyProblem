from typing import Any, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def solve_iter(root: Node):
	if not root.left or not root.right:
		return False

	sums = [0, 0]
	for i, start in enumerate([root.left, root.right]):
		remaining = [start]
		while remaining:
			current = remaining.pop()
			sums[i] += current.value
			for node in (current.left, current.right):
				if node:
					remaining.append(node)

	return len(set(sums)) == 1


def solve_recur(root: Node) -> bool:
	if not root.left or not root.right:
		return False

	def sumTree(root: Optional[Node]) -> int:
		return 0 if root is None else sumTree(root.left) + root.value + sumTree(root.right)

	return sumTree(root.left) == sumTree(root.right)


def test_solve():
	for solve in (solve_iter, solve_recur):
		root = Node(0,
			Node(-7, Node(-3, Node(4), Node(5)), Node(10, Node(2), Node(11))),
			Node(-13, Node(1, None, Node(9)), Node(8, Node(-12), Node(14)))
		)
		assert solve(root) is False
		assert solve(root.right) is True  # type: ignore
		assert solve(Node(1, Node(2, Node(3)))) is False
