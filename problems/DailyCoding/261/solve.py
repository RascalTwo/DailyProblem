import heapq

from typing import Dict, List, Optional, Tuple



class Node:
	def __init__(self, letter: Optional['str'] = None, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.letter = letter
		self.left = left
		self.right = right


	def find(self, letter: str) -> Tuple[bool, str]:
		if self.letter == letter:
			return True, ''

		for i, child in enumerate((self.left, self.right)):
			if not child:
				continue
			if child.letter == letter:
				return True, str(i)
			found, path = child.find(letter)
			if found:
				return True, str(i) + path

		return False, ''


	def encode(self, string: str) -> Optional[str]:
		results = ''
		for char in string:
			found, encoding = self.find(char)
			if not found:
				return
			results += encoding
		return results


	def decode(self, binary: str) -> Optional[str]:
		results = ''
		current: Optional[Node] = self
		for digit in binary:
			if digit == '1':
				current = current.right
			elif digit == '0':
				current = current.left
			if not current:
				return
			if current.letter:
				results += current.letter
				current = self
		return results


def solve(letters: Dict[str, int]) -> Node:
	nodes: List[Tuple[int, int, Node]] = [(frequency, i, Node(letter)) for i, (letter, frequency) in enumerate(letters.items())]
	heapq.heapify(nodes)

	while len(nodes) > 1:
		one = heapq.heappop(nodes)
		two = heapq.heappop(nodes)
		nodes.append((one[0] + two[0], one[1], Node(None, one[2], two[2])))

	return nodes[0][2]


def test_solve():
	tree = solve({'c': 1, 'a': 1, 't': 1, 's': 1})
	assert tree.encode('cats') == '00011011'
	assert tree.decode('00011011') == 'cats'
	assert tree.encode('dogs') is None
