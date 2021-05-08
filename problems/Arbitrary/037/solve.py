from typing import List



def solve(matrix: List[List[int]]) -> bool:
	rows = len(matrix)
	columns = len(matrix[0])

	if any(dim < 2 for dim in (rows, columns)):
		return False

	for top in range(rows):
		for left in range(columns):
			if matrix[top][left] == 1:
				for bottom in range(top + 1, rows):
					if matrix[bottom][left] == 1:
						for right in range(left + 1, columns):
							if matrix[top][right] == 1 and matrix[bottom][right] == 1:
								return True

	return False


def test_solve():
	assert solve([
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
	]) is False
	assert solve([
		[1, 1, 0, 0, 0],
		[1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
	]) is True
	assert solve([
		[1, 0, 1, 0, 0],
		[1, 1, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
	]) is False
	assert solve([
		[1, 1, 1, 0, 0],
		[1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[1, 0, 1, 0, 0],
		[0, 0, 0, 0, 0],
	]) is True
test_solve()