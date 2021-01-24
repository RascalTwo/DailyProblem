from typing import Dict, List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'], right: Optional['Node']):
		self.value = value
		self.left = left
		self.right = right


def tree_to_layers(root: Node, depth: int = 0) -> Dict[int, List[int]]:
	results = { depth: [root.value] }
	if root.left:
		for cdepth, values in tree_to_layers(root.left, depth + 1).items():
			results[cdepth] = results.get(cdepth, []) + values

	if root.right:
		for cdepth, values in tree_to_layers(root.right, depth + 1).items():
			results[cdepth] = results.get(cdepth, []) + values
	return results


def solve(root: Node):
	for layer_list in tree_to_layers(root).values():
		yield from layer_list


def test_solve():
	assert list(solve(Node(1, Node(2, None, None), Node(3, Node(4, None, None), Node(5, None, None))))) == [1, 2, 3, 4, 5]
