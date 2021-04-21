from typing import Any, Dict, Iterable, List, Optional, Tuple



class Trie:
	def __init__(self):
		self.children: Dict[str, Trie] = {}
		self.is_word = False


	def add_word(self, word: str):
		if not word:
			self.is_word = True
			return
		child = self.children.setdefault(word[0], Trie())
		child.add_word(word[1:])


	def __contains__(self, value: Any):
		return value in self.children


	def __getitem__(self, key: Any):
		return self.children[key]



def solve_iter(board: List[List[str]], words: List[str]) -> Iterable[str]:
	remaining = Trie()
	for word in words:
		remaining.add_word(word)

	states = [
		(
			[(r, c)],
			remaining[board[r][c]]
		)
		for r in range(len(board))
		for c in range(len(board[r]))
		if board[r][c] in remaining
	]

	while states and words:
		path, remaining = states.pop()
		r, c = path[-1]
		current_chars = ''.join(board[px][py] for px, py in path)

		if not any(word.startswith(current_chars) for word in words):
			continue

		if remaining.is_word:
			words.remove(current_chars)
			yield current_chars

		states.extend([
			(
				path + [(nextR, nextC)],
				remaining[board[nextR][nextC]]
			)
			for nextR, nextC in [
				(r + rOffset, c + cOffset)
				for rOffset, cOffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]
			]
			if (
				(nextR, nextC) not in path and
				0 <= nextR < len(board) and
				0 <= nextC < len(board[nextR]) and
				board[nextR][nextC] in remaining
			)
		])


def solve_recur(board: List[List[str]], words: List[str], path: List[Tuple[int, int]] = [], remaining: Optional[Trie] = None) -> Iterable[str]:
	if not path and not remaining:
		remaining = Trie()
		for word in words:
			remaining.add_word(word)

		for found in (
			solve_recur(
				board,
				words,
				[(r, c)],
				remaining[board[r][c]]
			)
			for r in range(len(board))
			for c in range(len(board[r]))
			if board[r][c] in remaining
		):
			yield from found
			if not words:
				break
		return

	assert remaining
	r, c = path[-1]
	current_chars = ''.join(board[px][py] for px, py in path)

	if not any(word.startswith(current_chars) for word in words):
		return

	if remaining.is_word:
		words.remove(current_chars)
		yield current_chars

	for found in (
		solve_recur(
			board,
			words,
			path + [(nextR, nextC)],
			remaining[board[nextR][nextC]]
		)
		for nextR, nextC in [
			(r + rOffset, c + cOffset)
			for rOffset, cOffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]
		]
		if (
			(nextR, nextC) not in path and
			0 <= nextR < len(board) and
			0 <= nextC < len(board[nextR]) and
			board[nextR][nextC] in remaining
		)
	):
		yield from found
		if not words:
			break


def test_solve():
	for solve in (solve_iter, solve_recur):
		assert sorted(list(solve([
			['o', 'a', 'a', 'n'],
			['e', 't', 'a', 'e'],
			['i', 'h', 'k', 'r'],
			['i', 'f', 'l', 'v']
		], ['oath', 'pea', 'eat', 'rain']))) == sorted(['eat', 'oath'])

		# size x size board with 1...size long words to find
		size = 50
		words = ['a' * n for n in range(1, size + 1)]
		assert sorted(list(solve(
			list(map(list, ['a' * size] * size)),
			words[:]
		))) == sorted(words)
