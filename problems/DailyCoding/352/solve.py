from typing import Iterable, List, Set, Tuple



def remove_letters(matrix: List[str]) -> Iterable[str]:
	for row in matrix:
		yield ''.join('W' if char.isalpha() else 'B' for char in row)


def traverse_whites(matrix: List[str], r: int, c: int, seen: Set[Tuple[int, int]]):
	loc = (r, c)
	if loc in seen:
		return
	if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[r]):
		return
	if matrix[r][c] != 'W':
		return

	seen.add(loc)
	traverse_whites(matrix, r - 1, c, seen)
	traverse_whites(matrix, r + 1, c, seen)
	traverse_whites(matrix, r, c - 1, seen)
	traverse_whites(matrix, r, c + 1, seen)


def solve(raw_matrix: List[str]) -> bool:
	matrix = list(remove_letters(raw_matrix))

	if matrix != [row[::-1] for row in reversed(matrix)]:
		return False

	whites: Set[Tuple[int, int]] = set()
	for r, row in enumerate(matrix):
		for c, char in enumerate(row):
			if char == 'W':
				whites.add((r, c))

	traversed: Set[Tuple[int, int]] = set()
	traverse_whites(matrix, *next(iter(whites)), traversed)
	if whites != traversed:
		return False

	processing = whites.copy()

	while processing:
		r, c = processing.pop()
		path: Set[Tuple[int, int]] = set()
		found_word = False
		for rd, cd in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			for _ in range(3):
				r += rd
				c += cd
				path.add((r, c))
				if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[r]):
					break
				if matrix[r][c] != 'W':
					break

			else:
				found_word = True

		if not found_word:
			return False

		for loc in path:
			processing.discard(loc)

	return True


def test_solve():
	assert solve([
		'USSR_',
		'META_',
		'MOONS',
		'_UNDO',
		'_LEOS'
	]) == True
	assert solve([
		'USSR_',
		'META_',
		'MOONS',
		'_UNDO',
		'OLEOS'
	]) == False
	assert solve([
		'USSR_',
		'META_',
		'M_O_S',
		'_UNDO',
		'_LEOS'
	]) == False
	assert solve([
		'USSR',
		'META',
	]) == False
