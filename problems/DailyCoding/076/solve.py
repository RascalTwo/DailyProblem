from typing import List


def solve(matrix: List[List[str]]) -> int:
	columns_started = len(matrix[0])

	for c in range(len(matrix[0]) - 1, -1, -1):
		valid_column = True
		last_letter = matrix[0][c]
		for r in range(1, len(matrix)):
			if (letter := matrix[r][c]) >= last_letter:
				last_letter = letter
			else:
				valid_column = False
				break

		if not valid_column:
			for r in range(len(matrix)):
				del matrix[r][c]

	return columns_started - len(matrix[0])


def test_solve():
	assert solve([
		['c', 'b', 'a'],
		['d', 'a', 'f'],
		['g', 'h', 'i'],
	]) == 1
	assert solve([
		['a', 'b', 'c', 'd', 'e', 'f']
	]) == 0
	assert solve([
		['z', 'y', 'x'],
		['w', 'v', 'u'],
		['t', 's', 'r'],
	]) == 3
