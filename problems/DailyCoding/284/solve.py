from typing import Any, Iterable, List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def solve(root: Node, target: Node) -> Iterable[Node]:
	if root == target:
		return []

	possible_nodes: List[Optional[Node]] = [root.left, root.right]
	while possible_nodes:
		nodes: List[Node] = [node for node in possible_nodes if node]
		for parent in nodes:
			if parent.left == target or parent.right == target:
				break
		else:
			possible_nodes = []
			for node in nodes:
				possible_nodes.extend([node.left, node.right])
			continue

		for node in nodes:
			if node != parent:
				yield from [child for child in (node.left, node.right) if child]
		break

	return []


def test_solve():
	tree = Node(1,
		Node(2, Node(5), Node(4)),
		Node(3, None, Node(6))
	)
	assert list(solve(tree, tree.left.left)) == [tree.right.right]  # type: ignore
	assert list(solve(tree, tree.right.right)) == [tree.left.left, tree.left.right]  # type: ignore
