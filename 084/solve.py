from typing import List


def flood_fill(matrix: List[List[int]], r: int, c: int):
	if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[c]) or matrix[r][c] != 1:
		return

	matrix[r][c] = 2
	flood_fill(matrix, r - 1, c)
	flood_fill(matrix, r, c + 1)
	flood_fill(matrix, r + 1, c)
	flood_fill(matrix, r, c - 1)


def solve(matrix: List[List[int]]) -> int:
	return sum(
		cell == 1 and (flood_fill(matrix, r, c) or 1)
		for r, row in enumerate(matrix)
		for c, cell in enumerate(row)
	)


def test_solve():
	assert solve([
		[1, 0, 0, 0, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0],
		[0, 0, 0, 0, 0],
		[1, 1, 0, 0, 1],
		[1, 1, 0, 0, 1]
	]) == 4
