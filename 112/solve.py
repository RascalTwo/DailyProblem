from typing import List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'], right: Optional['Node']):
		self.value = value

		if left:
			left.parent = self
		self.left = left

		if right:
			right.parent = self
		self.right = right

		self.parent: Optional['Node'] = None


def solve(root: Node, a: int, b: int) -> Optional[int]:
	if a != root.value and b != root.value:
		for child in (root.left, root.right):
			if not child:
				continue
			lca = solve(child, a, b)
			if lca is not None:
				return lca
		return None

	found = a if a == root.value else b
	other = a if found == b else b
	ancestor = root.parent
	assert ancestor

	decendants: List[Node] = [child for child in (ancestor.left, ancestor.right) if child]
	while decendants and ancestor:
		node = decendants.pop()
		if node.value == other:
			return ancestor.value
		for child in (node.left, node.right):
			if not child:
				continue
			if child.value == other:
				return ancestor.value
			decendants.append(child)

		if not decendants:
			previous = ancestor
			ancestor = ancestor.parent
			assert ancestor
			if ancestor.left and ancestor.left.value == previous.value:
				if ancestor.right:
					decendants.append(ancestor.right)
			if ancestor.right and ancestor.right.value == previous.value:
				if ancestor.left:
					decendants.append(ancestor.left)

	return None


def test_solve():
	root = Node(1,
		Node(2,
			Node(3, None, None),
			Node(4, None, None)
		),
		Node(5,
			Node(6, None, None),
			Node(7, None, None)
		)
	)
	assert solve(root, 6, 7) == 5
	assert solve(root, 5, 6) == 1
	assert solve(root, 3, 7) == 1
