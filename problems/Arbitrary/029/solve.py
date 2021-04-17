from typing import List, Tuple



def solve_iter(board: List[List[str]], word: str) -> bool:
	if not word:
		return False

	next_char = word[0]
	paths = [
		[(r, c)]
		for r in range(len(board))
		for c in range(len(board[r]))
		if board[r][c] == next_char
	]

	while paths:
		path = paths.pop()
		r, c = path[-1]
		next_char = word[len(path)]

		for nextR, nextC in [(r + rOffset, c + cOffset) for rOffset, cOffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
			if (
				(nextR, nextC) in path or
				nextR < 0 or nextR >= len(board) or
				nextC < 0 or nextC >= len(board[nextR]) or
				board[nextR][nextC] != next_char
			):
				continue

			if len(path) == len(word) - 1:
				return True

			paths.append(
				path + [(nextR, nextC)]
			)

	return False


def solve_recur(board: List[List[str]], word: str, path: List[Tuple[int, int]] = []) -> bool:
	next_char = word[len(path)]

	if not path:
		return any(
			solve_recur(board, word, [(r, c)])
			for r in range(len(board))
			for c in range(len(board[r]))
			if board[r][c] == next_char
		)


	r, c = path[-1]
	return any(
		len(path) == len(word) - 1 or solve_recur(board, word, path + [(nextR, nextC)])
		for nextR, nextC in [
			(r + rOffset, c + cOffset)
			for rOffset, cOffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]
		]
		if (
			(nextR, nextC) not in path and
			0 <= nextR < len(board) and
			0 <= nextC < len(board[nextR]) and
			board[nextR][nextC] == next_char
		)
	)



def test_solve():
	for solve in (solve_iter, solve_recur):
		assert solve([
			['a', 'b', 'c', 'e'],
			['s', 'f', 'c', 's'],
			['a', 'd', 'e', 'e']
		], 'abcced') is True

		assert solve([
			['a', 'b', 'c', 'e'],
			['s', 'f', 'c', 's'],
			['a', 'd', 'e', 'e']
		], 'sadsadasads') is False

		assert solve([
			['0', 'd', '0', '0'],
			['0', 'c', '0', '0'],
			['a', 'b', 'c', '0'],
			['0', '0', '0', '0']
		], 'abcd') is True

		assert solve([
			['0', '0', '0', '0'],
			['0', 'c', '0', '0'],
			['a', 'b', 'c', '0'],
			['0', '0', 'd', '0']
		], 'abcd') is True