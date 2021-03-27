from typing import List



def solve(matrix: List[List[int]], r: int = 0, c: int = 0) -> int:
	if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[r]) or matrix[r][c] == 1:
		return 0

	if r == len(matrix)-1 and c == len(matrix[r])-1:
		return 1

	return solve(matrix, r + 1, c) + solve(matrix, r, c + 1)


def test_solve():
	for matrix, paths in [
		([
			[0, 0, 1],
			[0, 0, 1],
			[1, 0, 0]
		], 2),
		([
			[0, 0, 1],
			[1, 0, 1],
			[1, 0, 0]
		], 1),
		([
			[0, 0, 0, 0],
			[0, 1, 1, 0],
			[0, 1, 1, 0],
			[0, 1, 1, 0],
			[0, 0, 0, 0]
		], 2),
		([
			[0, 0, 0, 0, 0],
			[0, 1, 1, 1, 0],
			[0, 1, 1, 1, 0],
			[0, 0, 0, 0, 0]
		], 2),
		([
			[0, 0],
			[0, 0]
		], 2),
		([
			[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]
		], 6),
		([
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]
		], 20)
	]:
		assert solve(matrix) == paths
