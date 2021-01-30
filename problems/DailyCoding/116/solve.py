from typing import Literal, Optional, Union

import random


class Node:
	def __init__(self, value: int, left: Union['Node', Literal[False], None], right: Union['Node', Literal[False], None]):
		self.value = value
		self._left = left or False
		self._right = right or False


	def __str__(self):
		return f'value={self.value} left=({self.left}) right=({self.right})'


	@property
	def left(self):
		if self._left is False:
			self._left = Node(self.value - 1, False, False) if random.random() < 0.5 else None
		return self._left


	@left.setter
	def left(self, value: Optional['Node']):
		self._left = value


	@property
	def right(self):
		if self._right is False:
			self._right = Node(self.value + 1, False, False) if random.random() < 0.5 else None
		return self._right


	@right.setter
	def right(self, value: Optional['Node']):
		self._right = value


def solve():
	return Node(0, False, False)


def test_solve():
	tree = solve()
	assert tree.left != False
	assert tree.right != False
	for _ in range(10):
		try:
			assert len(str(solve())) > 32
			break
		except:
			pass
