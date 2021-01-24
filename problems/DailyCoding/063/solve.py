from typing import List



def solve(matrix: List[List[str]], target: str):
	target_len = len(target)
	max_index = (len(matrix) - target_len) + 1
	for row in matrix:
		for i in range(max_index):
			if ''.join(row[i:i + target_len]) == target:
				return True

	for col in range(len(matrix)):
		for i in range(max_index):
			if ''.join(matrix[row][col] for row in range(i, i + target_len)) == target:
				return True

	return False


def test_solve():
	assert solve([
		['F', 'A', 'C', 'I'],
		['O', 'B', 'Q', 'P'],
		['A', 'N', 'O', 'B'],
		['M', 'A', 'S', 'S']
	], 'FOAM') is True
	assert solve([
		['F', 'A', 'C', 'I'],
		['O', 'B', 'Q', 'P'],
		['A', 'N', 'O', 'B'],
		['M', 'A', 'S', 'S']
	], 'MASS') is True
	assert solve([
		['F', 'A', 'C', 'I'],
		['O', 'B', 'Q', 'P'],
		['A', 'N', 'O', 'B'],
		['M', 'A', 'S', 'S']
	], 'NOB') is True
	assert solve([
		['F', 'A', 'C', 'I'],
		['O', 'B', 'Q', 'P'],
		['A', 'N', 'O', 'B'],
		['M', 'A', 'S', 'S']
	], 'BS') is True
