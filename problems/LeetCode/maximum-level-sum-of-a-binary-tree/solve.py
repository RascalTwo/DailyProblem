import collections

from typing import DefaultDict, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node) -> int:
	sums: DefaultDict[int, int] = collections.defaultdict(int)

	def add(node: Node, depth: int):
		sums[depth] += node.value
		for child in (node.left, node.right):
			if child:
				add(child, depth + 1)

	add(root, 1)

	return max(sums.items(), key = lambda item: item[1])[0]


def test_solve():
	assert solve(Node(1, Node(7, Node(0, Node(7, Node(-8)))))) == 2
	assert solve(Node(989, Node(10250, Node(98693), Node(-89388, Node(-32127))))) == 2