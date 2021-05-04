from typing import List



def solve(matrix: List[List[int]]) -> bool:
	edges = 0
	for r, row in enumerate(matrix):
		for c in row[r:]:
			if c:
				edges += 1
	return edges == len(matrix) - 1


def test_solve():
	assert solve([
		[0, 1, 0, 0, 1],
		[1, 0, 1, 1, 1],
		[0, 1, 0, 1, 0],
		[0, 1, 1, 0, 1],
		[1, 1, 0, 1, 0],
	]) is False
	assert solve([
		[0, 1, 1],
		[0, 0, 0],
		[0, 0, 0],
	]) is True
