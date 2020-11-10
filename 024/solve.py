from typing import Optional



class Node:
	def __init__(self, lock: bool = False, left: Optional['Node'] = None, right: Optional['Node'] = None, parent: Optional['Node'] = None):
		self.is_locked = lock
		self.left = left
		self.right = right
		self.parent = parent


	def is_mutable(self, immutable_state: bool) -> bool:
		if self.is_locked is immutable_state:
			return False

		ancestor = self.parent
		while ancestor:
			if ancestor.is_locked:
				return False
			ancestor = ancestor.parent

		return (
			(self.left.is_mutable(True) if self.left else True)
			and
			(self.right.is_mutable(True) if self.right else True)
		)


	def _mutate(self, locked: bool) -> bool:
		if not self.is_mutable(locked):
			return False

		self.is_locked = locked
		return True


	def lock(self) -> bool:
		return self._mutate(True)


	def unlock(self) -> bool:
		return self._mutate(False)


def test_solve():
	root = Node(False, None, None, None)
	root.left = Node(False, None, None, root)
	root.left.left = Node(True, None, None, root.left)
	root.left.right = Node(False, None, None, root.left)
	root.right = Node(False, None, None, root)

	assert root.lock() is False
	assert root.right.lock() is True
	assert root.right.unlock() is True
	assert root.left.left.unlock() is True
	assert root.lock() is True
	assert root.right.unlock() is False
