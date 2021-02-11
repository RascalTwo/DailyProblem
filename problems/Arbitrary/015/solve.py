from typing import List



def solve(board: List[List[str]]) -> int:
	PIECES = ['X', 'O']
	size = len(board)

	def winner_index(values: List[str]) -> int:
		if values == [values[0]] * size and values[0] in PIECES:
			return PIECES.index(values[0]) + 1
		return 0

	# horizontal
	for row in board:
		if index := winner_index(row):
			return index

	# vertical
	for c in range(size):
		if index := winner_index([row[c] for row in board]):
			return index

	# diagnal
	for (r, c), (vr, vc) in [((0, 0), (1, 1)), ((0, size - 1), (1, -1))]:
		if index := winner_index([board[r + (vr * i)][c + (vc * i)] for i in range(size)]):
			return index

	# in progress
	for row in board:
		for cell in row:
			if cell not in PIECES:
				return 0

	return 3


def test_solve():
	assert solve([
		['X', 'X', 'X'],
		['O', 'O', 'X'],
		['O', 'X', 'O']
	]) == 1
	assert solve([
		[' ', ' ', 'O'],
		[' ', 'X', ' '],
		[' ', ' ', 'O']
	]) == 0
	assert solve([
		['O', ' ', ' ', ' '],
		[' ', 'O', ' ', ' '],
		[' ', ' ', 'O', ' '],
		[' ', ' ', ' ', 'O'],
	]) == 2
	assert solve([
		[' ', ' ', ' ', 'X'],
		[' ', ' ', 'X', ' '],
		[' ', 'X', ' ', ' '],
		['X', ' ', ' ', ' '],
	]) == 1
	assert solve([
		[' ', ' ', 'O', ' '],
		[' ', ' ', 'O', ' '],
		[' ', ' ', 'O', ' '],
		[' ', ' ', 'O', ' '],
	]) == 2
	assert solve([
		['X', 'O', 'X', 'O'],
		['X', 'O', 'X', 'O'],
		['O', 'X', 'O', 'X'],
		['O', 'X', 'O', 'X'],
	]) == 3
	print('solve passed')
