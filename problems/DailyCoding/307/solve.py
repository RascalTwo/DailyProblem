from typing import Any, Optional, Tuple



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.left == other.left and self.right == other.right


def solve_iter(root: Node, target: int) -> Tuple[Optional[Node], Optional[Node]]:
	floor: Optional[Node] = None

	new_floors = []
	floors = [root]
	while floors:
		node = floors.pop()
		if node.value <= target and (not floor or abs(node.value - target) < abs(floor.value - target)):
			floor = node

		new_floors.extend(filter(bool, (node.left, node.right)))
		if not floors and not floor:
			floors = new_floors
			new_floors = []


	ceiling: Tuple[Optional[Node], int] = (None, -1)
	depth = 0
	new_ceilings = []
	ceilings = [root]
	while ceilings:
		node = ceilings.pop()
		if node.value >= target and depth > ceiling[1] and (not ceiling[0] or abs(node.value - target) < abs(ceiling[0].value - target)):
			ceiling = node, depth

		new_ceilings.extend(filter(bool, (node.left, node.right)))
		if not ceilings:
			ceilings = new_ceilings
			new_ceilings = []
			depth += 1


	return floor, ceiling[0]


def recur_node(node: Optional[Node], target: int, type: str, depth: int = 0) -> Optional[Tuple[Node, int]]:
	if not node:
		return None

	if type == 'floor':
		if node.value <= target:
			return node, depth

	left = recur_node(node.left, target, type, depth + 1)
	right = recur_node(node.right, target, type, depth + 1)
	if left and right:
		return min((left, right), key = lambda child: (-child[1], abs(child[0].value - target)))

	if type == 'ceil':
		if node.value >= target:
			return node, depth

	return left or right



def solve_recur(root: Node, target: int) -> Tuple[Optional[Node], ...]:
	return tuple(
		(recur_node(root, target, type) or (None, -1))[0]
		for type in ('floor', 'ceil')
	)


def test_solve():
	tree = Node(5,
		Node(6,
			Node(8),
			Node(7)
		),
		Node(2,
			Node(0),
			Node(3,
				Node(4)
			)
		)
	)
	for solve in (solve_iter, solve_recur):
		assert solve(tree, 3) == (tree.right, tree.right.right)
		assert solve(tree, 7) == (tree, tree.left.right)
