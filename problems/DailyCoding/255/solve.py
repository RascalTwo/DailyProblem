from typing import List



def solve(adjacency_list: List[List[int]]) -> List[List[int]]:
	transitive_closure: List[List[int]] = [[0 for _ in range(len(adjacency_list))] for _ in range(len(adjacency_list))]

	for row in adjacency_list:
		for destination in row:
			transitive_closure[row[0]][destination] = 1

	return transitive_closure


def test_solve():
	assert solve([
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
	]) == [
		[1, 1, 0, 1],
		[0, 1, 1, 0],
		[0, 0, 1, 0],
		[0, 0, 0, 1]
	]
