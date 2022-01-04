from typing import Dict



def tour(board: Dict[complex, bool], current: complex) -> int:
	board[current] = True
	if all(seen for seen in board.values()):
		return 1

	tours = 0
	for offset in (-2+-1j, -2+1j, -1+2j, 1+2j, 2+1j, 2+-1j, 1+-1j, -1+-2j):
		attempt = current + offset
		if board.get(attempt, True) is False:
			tours += tour(board.copy(), attempt)
	return tours


def solve(n: int) -> int:
	board: Dict[complex, bool] = {}
	for r in range(n):
		for c in range(n):
			board[complex(r, c)] = False


	tours = 0
	for start in board.keys():
		tours += tour(board.copy(), start)

	return tours


def test_solve():
	assert solve(1) == 1
	assert solve(2) == 0
	assert solve(3) == 10
	assert solve(4) == 16