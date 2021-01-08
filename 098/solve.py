from typing import List, Tuple



def find_word(board: List[List[str]], r: int, c: int, word: str, path: List[Tuple[int, int]]) -> bool:
	if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]) or (r, c) in path:
		return False

	if board[r][c] != word[0]:
		return False

	if len(word) == 1:
		return True

	path.append((r, c))
	for ro, co in ((-1, 0), (0, 1), (1, 0), (0, -1)):
		if find_word(board, r + ro, c + co, word[1:], path[:]):
			return True

	return False


def solve(board: List[List[str]], word: str):
	start = word[0]
	for r, row in enumerate(board):
		for c, col in enumerate(row):
			if col != start:
				continue
			if find_word(board, r, c, word, []):
				return True
	return False


def test_solve():
	board = [
		['A','B','C','E'],
		['S','F','C','S'],
		['A','D','E','E']
	]
	assert solve(board, 'ABCCED') is True
	assert solve(board, 'SEE') is True
	assert solve(board, 'ABCB') is False
