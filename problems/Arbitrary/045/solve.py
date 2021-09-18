from typing import List, Set, Tuple



def collect_island(matrix: List[List[int]], seen: Set[Tuple[int, int]], r: int, c: int) -> Set[Tuple[int, int]]:
	seen.add((r, c))

	for ro, co in [
		(0, 1), (0, -1), (1, 0), (-1, 0)
	]:
		nr, nc = r + ro, c + co
		if (nr, nc) in seen:
			continue
		if nr < 0 or nr >= len(matrix) or nc < 0 or nc >= len(matrix[nr]):
			continue
		if matrix[nr][nc] != 1:
			continue

		collect_island(matrix, seen, nr, nc)

	return seen


def is_edge(matrix: List[List[int]], r: int, c: int) -> bool:
	return r == 0 or r == len(matrix)-1 or c == 0 or c == len(matrix[r])-1


def solve(matrix: List[List[int]]) -> List[List[int]]:
	processed: Set[Tuple[int, int]] = set()

	for r, row in enumerate(matrix):
		for c, col in enumerate(row):
			if col == 0 or (r, c) in processed:
				processed.discard((r, c))  # free up unused memory
				continue

			coords = collect_island(matrix, set(), r, c)
			if any(is_edge(matrix, r, c) for r, c in coords):
				processed |= coords
			else:
				for cr, cc in coords:
					matrix[cr][cc] = 0

	return matrix


def test_solve():
	assert solve([
		[1, 0, 0, 0, 0, 0],
		[0, 1, 0, 1, 1, 1],
		[0, 0, 1, 0, 1, 0],
		[1, 1, 0, 0, 1, 0],
		[1, 0, 1, 1, 0, 0],
		[1, 0, 0, 0, 0, 1],
	]) == [
		[1, 0, 0, 0, 0, 0],
		[0, 0, 0, 1, 1, 1],
		[0, 0, 0, 0, 1, 0],
		[1, 1, 0, 0, 1, 0],
		[1, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 1],
	]
	assert solve([
		[1, 0, 0, 0, 0, 0],
		[0, 1, 0, 0, 1, 1],
		[0, 0, 1, 1, 0, 0],
		[1, 0, 1, 1, 0, 0],
		[1, 0, 1, 1, 0, 0],
		[1, 0, 0, 0, 0, 1],
	]) == [
		[1, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1],
		[0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 1],
	]
