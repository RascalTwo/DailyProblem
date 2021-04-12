from typing import List



def solve(matrix: List[List[int]]) -> List[List[int]]:
	return [
		[
			matrix[r][c]
			for r in range(len(matrix[c]) - 1, -1, -1)
		]
		for c in range(len(matrix))
	]


def test_solve():
	assert solve([
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]) == [
		[7, 4, 1],
		[8, 5, 2],
		[9, 6, 3]
	]
