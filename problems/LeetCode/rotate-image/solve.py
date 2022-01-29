from typing import List



def solve(matrix: List[List[int]]):
	size = len(matrix)
	for ring in range(size // 2):
		opposite = size - ring - 1
		for cell in range(size - (2 * ring) - 1):
			temp = matrix[ring][ring + cell]
			matrix[ring][ring + cell] = matrix[opposite - cell][ring]
			matrix[opposite - cell][ring] = matrix[opposite][opposite - cell]
			matrix[opposite][opposite - cell] = matrix[ring + cell][opposite]
			matrix[ring + cell][opposite] = temp

	return matrix


def test_solve():
	assert solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
	assert solve([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]) == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
