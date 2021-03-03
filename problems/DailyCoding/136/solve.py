from typing import List



def flood_fill(matrix: List[List[int]], r: int, c: int) -> int:
	if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[r]) or matrix[r][c] != 1:
		return 0

	matrix[r][c] = 2

	return (
		1 +
		flood_fill(matrix, r - 1, c) +
		flood_fill(matrix, r, c - 1) +
		flood_fill(matrix, r + 1, c) +
		flood_fill(matrix, r, c + 1)
	)



def solve(matrix: List[List[int]]) -> int:
	most = 0

	for r, row in enumerate(matrix):
		for c, cell in enumerate(row):
			if cell == 1:
				most = max(most, flood_fill(matrix, r, c))

	return most


def test_solve():
	assert solve([
		[1, 0, 0, 0],
		[1, 0, 1, 1],
		[1, 0, 1, 1],
		[0, 1, 0, 0]
	]) == 4
test_solve()