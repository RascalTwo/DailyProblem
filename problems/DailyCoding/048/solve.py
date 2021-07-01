from typing import Any, List, Optional



class Node:
	def __init__(self, value: str, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right

	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def preorder(traversal: List[str]) -> Optional[Node]:
	if not traversal:
		return None
	root = Node(traversal.pop(0))
	middle = len(traversal) // 2
	root.left = preorder(traversal[:middle])
	root.right = preorder(traversal[middle:])
	return root


def inorder(traversal: List[str]) -> Optional[Node]:
	if not traversal:
		return None
	middle = len(traversal) // 2
	root = Node(traversal.pop(middle))
	root.left = inorder(traversal[:middle])
	root.right = inorder(traversal[middle:])
	return root


def test_solve():
	tree = Node('a',
		Node('b', Node('d'), Node('e')),
		Node('c', Node('f'), Node('g'))
	)
	assert preorder(['a', 'b', 'd', 'e', 'c', 'f', 'g']) == tree
	assert inorder(['d', 'b', 'e', 'a', 'f', 'c', 'g']) == tree
