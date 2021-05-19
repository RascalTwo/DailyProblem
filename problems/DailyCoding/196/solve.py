import collections


from typing import Counter, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node) -> int:
	counter: Counter[int] = collections.Counter()
	def recur(node: Optional['Node']) -> int:
		if not node:
			return 0
		sum = node.value + recur(node.left) + recur(node.right)
		counter[sum] += 1
		return sum
	recur(root)
	return sorted(counter.items(), key=lambda pair: pair[1], reverse=True)[0][0]


def test_solve():
	assert solve(Node(5, Node(2), Node(-5))) == 2
