from typing import Optional


class Node:
	def __init__(self, char: str, is_word: bool, left: Optional['Node'] = None, middle: Optional['Node'] = None, right: Optional['Node'] = None):
		self.char	= char
		self.is_word = is_word
		self.left	= left
		self.middle	= middle
		self.right = right


class TST:
	def __init__(self):
		self.root: Optional[Node] = None

	def _insert(self, node: Node, word: str) -> None:
		if word[0] < node.char:
			if not node.left:
				node.left = Node(word[0], False)
			return self._insert(node.left, word)
		elif word[0] > node.char:
			if not node.right:
				node.right = Node(word[0], False)
			return self._insert(node.right, word)

		if len(word) > 1:
			if not node.middle:
				node.middle = Node(word[1], False)
			return self._insert(node.middle, word[1:])

		node.is_word = True

	def insert(self, word: str):
		if not self.root:
			self.root = Node(word[0], False)
		return self._insert(self.root, word)


	def _contains(self, node: Optional[Node], word: str) -> bool:
		if not word:
			return True
		if not node:
			return False

		if word[0] < node.char:
			return self._contains(node.left, word)
		elif word[0] > node.char:
			return self._contains(node.right, word)
		return self._contains(node.middle, word[1:])


	def __contains__(self, word: str) -> bool:
		return self._contains(self.root, word)



def test_solve():
	words = ('code', 'cob', 'be', 'ax', 'war', 'we')
	tst = TST()
	for word in words:
		tst.insert(word)

	for word in words:
		assert word in tst

	assert 'codey' not in tst
	assert 'coa' not in tst
	assert 'abc' not in tst
