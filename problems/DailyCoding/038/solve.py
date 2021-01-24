import copy


from typing import Iterable, List, TypeVar



T = TypeVar('T')
Matrix = List[List[T]]


def is_placable(board: Matrix[bool], qr: int, qc: int) -> bool:
	for c, col in enumerate(board[qr]):
		if c != qc and col:
			return False

	for r in range(len(board)):
		if r != qr and board[r][qc]:
			return False

	r, c = qr - 1, qc - 1
	while r >= 0 and c >= 0:
		if board[r][c]:
			return False
		r -= 1
		c -= 1

	r, c = qr + 1, qc + 1
	while r < len(board) and c < len(board[r]):
		if board[r][c]:
			return False
		r += 1
		c += 1

	r, c = qr - 1, qc + 1
	while r >= 0 and c < len(board[r]):
		if board[r][c]:
			return False
		r -= 1
		c += 1


	r, c = qr + 1, qc - 1
	while r < len(board) and c >= 0:
		if board[r][c]:
			return False
		r += 1
		c -= 1

	return True


def test_is_placable():
	board = [[False, False, False],[False, False, False],[False, False, False]]
	assert is_placable(board, 0, 0) is True

	for (r, c), (qr, qc) in (
		((0, 2), (0, 0)),  # Horizontal right
		((0, 0), (0, 2)),  # Horizontal left
		((1, 0), (1, 2)),  # Vertical up
		((1, 2), (1, 0)),  # Vertical down
		((0, 0), (2, 2)),  # Diagonal up-left
		((2, 2), (0, 0)),  # Diagonal down-right
		((0, 2), (2, 0)),  # Diagonal up-right
		((2, 0), (0, 2)),  # Diagonal down-left
	):
		board[r][c] = True
		assert is_placable(board, qr, qc) is False
		board[r][c] = False


def place_nth_queen(board: Matrix[bool], queen: int, total: int) -> Iterable[Matrix[bool]]:
	if queen == total:
		yield copy.deepcopy(board)
		return

	for r, row in enumerate(board):
		for c, col in enumerate(row):
			if not col and is_placable(board, r, c):
				board[r][c] = True
				yield from place_nth_queen(board, queen + 1, total)
				board[r][c] = False


def solve(total: int) -> int:
	board = [[False] * total for _ in range(total)]

	solutions = []
	for solution in place_nth_queen(board, 0, total):
		if solution not in solutions:
			solutions.append(solution)

	return len(solutions)


def test_solve():
	assert solve(4) == 2
	assert solve(5) == 10
	assert solve(6) == 4
	assert solve(7) == 40
