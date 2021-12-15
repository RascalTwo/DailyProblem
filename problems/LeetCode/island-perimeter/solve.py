from typing import List



def solve(grid: List[List[int]]):
	edges = 0

	for r, row in enumerate(grid):
		for c, cell in enumerate(row):
			if not cell:
				continue
			for nr, nc in [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]:
				if (nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[nr])) or grid[nr][nc] == 0:
					edges += 1

	return edges


def test_solve():
	assert solve([[1]]) == 4
	assert solve([
		[0, 1, 1, 0],
		[1, 1, 1, 0],
		[0, 1, 1, 0],
		[0, 0, 1, 0]
	]) == 14
	assert solve([
		[0, 1, 0, 0],
		[1, 1, 1, 0],
		[0, 1, 0, 0],
		[1, 1, 0, 0]
	]) == 16
