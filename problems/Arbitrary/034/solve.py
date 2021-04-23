from typing import Any, List, Optional, Set



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


	def __hash__(self):
		return hash(self.value) + hash(self.left) + hash(self.right)


def build_path(root: Optional[Node], path: List[Node], target: Node):
	if root is None:
		return

	path.insert(0, root)

	if root == target or any(child and build_path(child, path, target) for child in (root.left, root.right)):
		return True

	path.pop(0)


def solve(root: Node, *nodes: Node):
	paths: List[List[Node]] = [[] for _ in range(len(nodes))]

	if not all(
		build_path(root, paths[i], node)
		for i, node in enumerate(nodes)
	):
		return


	prev: Optional[Set[Node]] = None
	while all(paths):
		values = set(path.pop() for path in paths)
		if len(values) != 1:
			return next(iter(prev)) if prev else None

		prev = values

	return next(iter(prev)) if prev else None


def test_solve():
	root = Node(3,
		Node(5,
			Node(6),
			Node(2,
				Node(7),
				Node(4)
			)
		),
		Node(1,
			Node(0),
			Node(8)
		)
	)
	assert solve(root, root.left, root.right) == root  # type: ignore
	assert solve(root, root.left.left, root.left.right) == root.left  # type: ignore
	assert solve(root, root.left.right.right, root.left.left) == root.left  # type: ignore
	assert solve(root, root.left, root.left.right.right) == root.left  # type: ignore
	assert solve(root, root.left, root.left.right.right, root.right) == root  # type: ignore
	assert solve(root, root.left, root.right, None) == None  # type: ignore
