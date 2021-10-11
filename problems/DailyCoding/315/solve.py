from typing import Iterable, List



def solve_diagonal(matrix: List[List[int]]) -> bool:
	rows = len(matrix)
	columns = len(matrix[0])

	for row, col in [
		(0, col)
		for col in range(columns)
	] + [
		(row, 0)
		for row in range(rows)
	]:
		last = matrix[row][col]
		while 0 <= row < rows and 0 <= col < columns:
			if matrix[row][col] != last:
				return False
			row += 1
			col += 1

	return True


def solve_iter(matrix: List[List[int]]) -> bool:
	for i, row in enumerate(matrix[:-1]):
		if row[:-1] != matrix[i + 1][1:]:
			return False

	return True


def generate_toeplitz(rows: int, columns: int) -> Iterable[List[int]]:
	values = list(range(columns))
	for _ in range(rows):
		yield values.copy()
		values.insert(0, values.pop())


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
		assert solve(list(generate_toeplitz(2500, 2500))) is True
