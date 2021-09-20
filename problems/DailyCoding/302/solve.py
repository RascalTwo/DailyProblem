from typing import List, Set, Tuple

Point = Tuple[int, int]

def flood_map(matrix: List[List[str]], seen: Set[Point], r: int, c: int) -> Set[Point]:
	seen.add((r, c))

	for ro, co in [
		(1, 0), (-1, 0), (0, 1), (0, -1)
	]:
		nr, nc = r + ro, c + co
		if (nr, nc) not in seen and 0 <= nr < len(matrix) and 0 <= nc < len(matrix[nr]) and matrix[nr][nc] == ' ':
			flood_map(matrix, seen, nr, nc)

	return seen


def solve(matrix: List[List[str]]) -> int:
	group_count = 0

	processed: Set[Point] = set()
	for r, row in enumerate(matrix):
		for c, col in enumerate(row):
			if col != ' ' or (r, c) in processed:
				continue

			processed |= flood_map(matrix, set(), r, c)
			group_count += 1

	return group_count


def test_solve():
	assert solve([
		list(r'\    /'),
		list(r' \  / '),
    list(r'  \/  ')
	]) == 3
	assert solve([
		list(r'\    /'),
		list(r'    / '),
    list(r'  \/  ')
	]) == 2
	assert solve([
		list(r'\         '),
		list(r' \        '),
		list(r'  \-------'),
		list(r'  / | |   '),
		list(r' /  \ /   '),
		list(r'/    -    '),
		list(r'          '),
		list(r'     /    '),
		list(r'    /     '),
		list(r'   /      '),
	]) == 4
