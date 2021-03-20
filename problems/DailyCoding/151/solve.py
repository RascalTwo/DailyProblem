from typing import List, Tuple



def flood_fill(matrix: List[List[str]], r: int, c: int, replacing: str, to: str):
	if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[c]) or matrix[r][c] != replacing:
		return

	matrix[r][c] = to
	flood_fill(matrix, r-1, c, replacing, to)
	flood_fill(matrix, r, c+1, replacing, to)
	flood_fill(matrix, r+1, c, replacing, to)
	flood_fill(matrix, r, c-1, replacing, to)


def solve(matrix: List[List[str]], location: Tuple[int, int], to: str) -> List[List[str]]:
	r, c = location[0], location[1]
	flood_fill(matrix, r, c, matrix[r][c], to)
	return matrix


def test_solve():
	assert solve([
		['B', 'B', 'W'],
		['W', 'W', 'W'],
		['W', 'W', 'W'],
		['B', 'B', 'B'],
	], (2, 2), 'G') == [
		['B', 'B', 'G'],
		['G', 'G', 'G'],
		['G', 'G', 'G'],
		['B', 'B', 'B'],
	]

	assert solve([
		['B', 'B', 'W'],
		['W', 'W', 'W'],
		['W', 'W', 'W'],
		['B', 'B', 'B'],
	], (0, 1), 'A') == [
		['A', 'A', 'W'],
		['W', 'W', 'W'],
		['W', 'W', 'W'],
		['B', 'B', 'B'],
	]
