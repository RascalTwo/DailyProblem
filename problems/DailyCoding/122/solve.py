from typing import List, Tuple



def solve(matrix: List[List[int]]) -> int:
	most = 0

	incomplete: List[List[Tuple[int, int]]] = [[(0, 0)]]
	while incomplete:
		path = incomplete.pop()
		r, c = path[-1]

		if new_paths := [
			path + [(nr, nc)]
			for vr, vc in ((1, 0), (0, 1))
			if (nr := r + vr) < len(matrix)
			and (nc := c + vc) < len(matrix[nr])
		]:
			incomplete += new_paths
			continue

		most = max(sum(matrix[r][c] for r, c in path), most)

	return most


def test_solve():
	assert solve([
		[0, 3, 1, 1],
		[2, 0, 0, 4],
		[1, 5, 3, 1]
	]) == 12
	assert solve([
		[0, 0, 5, 0, 5],
		[2, 3, 0, 0, 0],
		[0, 2, 3, 0, 5],
		[0, 0, 2, 3, 0],
		[0, 0, 0, 2, 5],
	]) == 22
