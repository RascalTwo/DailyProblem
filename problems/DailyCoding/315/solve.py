from typing import List



def solve_diagonal(matrix: List[List[int]]) -> bool:
	for row, col in [
		(0, col)
		for col in range(len(matrix[0]))
	] + [
		(row, 0)
		for row in range(len(matrix))
	]:
		last = matrix[row][col]
		while 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
			if matrix[row][col] != last:
				return False
			row += 1
			col += 1

	return True


def solve_iter(matrix: List[List[int]]) -> bool:
	for i, row in enumerate(matrix[:-1]):
		if row[:-1] != matrix[i+1][1:]:
			return False

	return True


def test_solve():
	for solve in (solve_iter, solve_diagonal):
		assert solve([
			[1, 2, 3, 4, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 4, 5, 1, 2],
		]) is True
		assert solve([
			[0, 2, 3, 4, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 4, 5, 1, 2],
		]) is False
		assert solve([
			[1, 2, 3, 0, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 4, 5, 1, 2],
		]) is False
		assert solve([
			[1, 2, 3, 0, 8],
			[5, 1, 2, 3, 4],
			[4, 5, 1, 2, 3],
			[7, 0, 5, 1, 2],
		]) is False
