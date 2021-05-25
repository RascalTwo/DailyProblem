import collections


from typing import DefaultDict, List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def build_tree(levels: List[List[int]]) -> Optional[Node]:
	if not levels or not levels[0]:
		return None
	root = Node(levels[0][0])
	root.left = build_tree([level[:-1] for level in levels[1:]])
	root.right = build_tree([level[1:] for level in levels[1:]])
	return root


def solve(levels: List[List[int]]) -> int:
	root = build_tree(levels)

	max_sum: DefaultDict[Optional[Node], int] = collections.defaultdict(int)
	def recur(node: Optional[Node]) -> int:
		if not node:
			return 0

		if node in max_sum:
			return max_sum[node]

		return max_sum.setdefault(node, max(
			node.value + (max_sum[child]
				if child in max_sum else
				max_sum.setdefault(child, recur(child))
			)
			for child in (node.left, node.right)
		))
	return recur(root)


def test_solve():
	assert solve([[1], [2, 3], [1, 5, 1]]) == 9
	assert solve([[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]) == 15
	assert solve([[1], [1, 1], [1, 1, 48], [1, 1, 1, 1], [1, 1, 49, 1, 1]]) == 100


