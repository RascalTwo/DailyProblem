from typing import Dict, List



class Trie:
	def __init__(self):
		self.value: int = 0
		self.children: Dict[str, Trie] = {}
		self.is_word = False


class PrefixMapSum:
	def __init__(self):
		self.data = Trie()

	def insert(self, key: str, value: int):
		traversed: List[Trie] = []
		current = self.data
		while key:
			traversed.append(current)
			current = result if (result := current.children.get(key[0], None)) else current.children.setdefault(key[0], Trie())
			key = key[1:]

		if current.is_word:
			value = -current.value + value
		current.is_word = True

		for trie in traversed + [current]:
			trie.value += value

	def sum(self, prefix: str) -> int:
		current = self.data
		while current and prefix:
			current = current.children.get(prefix[0], None)
			prefix = prefix[1:]

		return current.value if current else 0


def test_solve():
	mapsum = PrefixMapSum()
	mapsum.insert('columnar', 3)
	assert mapsum.sum('col') == 3

	mapsum.insert('column', 2)
	assert mapsum.sum('col') == 5

	mapsum.insert('columnar', 0)
	assert mapsum.sum('col') == 2

	mapsum.insert('column', 0)
	assert mapsum.sum('col') == 0

	mapsum.insert('columnar', 10)
	assert mapsum.sum('col') == 10

	assert mapsum.sum('abc') == 0
