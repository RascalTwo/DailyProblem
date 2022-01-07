import collections

from typing import Dict, List, Optional, Set, Tuple

Options = Dict[Tuple[int, int], Set[int]]
SquareOptions = Tuple[int, int, Options]


def is_valid_square(square: List[List[Optional[int]]]):
	seen: Set[int] = set()
	for row in square:
		for cell in row:
			if cell is None or cell in seen:
				return False
			seen.add(cell)

	return True


def is_valid_sudoku(puzzle: List[List[Optional[int]]]) -> bool:
	for start_row in (0, 3, 6):
		for start_col in (0, 3, 6):
			if not is_valid_square([row[start_col:start_col + 3] for row in puzzle[start_row:start_row + 3]]):
				return False

	return True


def get_least_options(a: Options, b: Options) -> Options:
	a_counts = collections.Counter(map(len, a.values()))
	b_counts = collections.Counter(map(len, b.values()))
	for least in range(1, 10):
		diff = a_counts.get(least, 9) - b_counts.get(least, 9)
		if diff:
			return a if diff < 0 else b

	return a



def solve(puzzle: List[List[Optional[int]]]):
	if is_valid_sudoku(puzzle):
		return puzzle

	most_restricted: Optional[SquareOptions] = None
	for start_row in (0, 3, 6):
		for start_col in (0, 3, 6):
			square = [row[start_col:start_col + 3] for row in puzzle[start_row:start_row + 3]]
			options: Options = {}
			for sr, row in enumerate(square):
				for sc, cell in enumerate(row):
					if cell:
						continue

					r, c = start_row + sr, start_col + sc
					values: Set[int] = set()
					for cr in range(len(puzzle)):
						if cr != r and (cell := puzzle[cr][c]):
							values.add(cell)
					for cc in range(len(puzzle[0])):
						if cc != c and (cell := puzzle[r][cc]):
							values.add(cell)
					for row in square:
						for cell in row:
							if cell:
								values.add(cell)
					options[sr, sc] = set(range(1, 10)) - values
			if most_restricted is None or get_least_options(most_restricted[2], options) == options:
				most_restricted = start_row, start_col, options


	assert most_restricted
	start_row, start_col, options = most_restricted
	square = [row[start_col:start_col + 3] for row in puzzle[start_row:start_row + 3]]
	(sr, sc), values = min(options.items(), key = lambda item: len(item[1]))
	r, c = start_row + sr, start_col + sc
	for value in values:
		puzzle[r][c] = value
		if solve(puzzle):
			return puzzle
		puzzle[r][c] = None

	return False


def test_solve():
	assert solve([
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None],
		[None, None, None, None, None, None, None, None, None]
	])
	assert solve([
		[3, 9, 5, 2, 7, 1, 4, 8, 6],
		[7, 4, 6, 8, 3, 5, 2, 1, 9],
		[8, 2, 1, 4, 6, 9, 5, 7, 3],
		[5, 3, 9, 7, 4, 8, 6, 2, 1],
		[2, 7, 8, 5, 1, 6, 9, 3, 4],
		[6, 1, 4, 3, 9, 2, 7, 5, 8],
		[9, 6, 2, 1, 8, 7, 3, 4, 5],
		[1, 5, 3, 6, 2, 4, 8, 9, 7],
		[4, 8, 7, 9, 5, 3, 1, 6, 2]
	])
	assert solve([
		[3, 9, 5, 2, 7, 1, 4, 8, 6],
		[7, 4, 6, 8, 3, 5, 2, 1, 9],
		[8, 2, 1, 4, 6, 9, 5, 7, 3],
		[5, 3, 9, 7, 4, 8, 6, 2, 1],
		[2, 7, 8, 5, 1, 6, 9, 3, 4],
		[6, 1, 4, 3, 9, 2, 7, 5, 8],
		[9, 6, 2, 1, 8, 7, 3, 4, 5],
		[1, 5, 3, 6, 2, 4, 8, 9, 7],
		[4, 8, 7, 9, 5, 3, 1, 6, None]
	])
	assert solve([
		[3, 9, 5, 2, 7, 1, 4, 8, None],
		[7, 4, 6, 8, 3, 5, 2, 1, None],
		[8, 2, 1, 4, 6, 9, 5, 7, None],
		[5, 3, 9, 7, 4, 8, 6, 2, None],
		[2, 7, 8, 5, 1, 6, 9, 3, None],
		[6, 1, 4, 3, 9, 2, 7, 5, None],
		[9, 6, 2, 1, 8, 7, 3, 4, None],
		[1, 5, 3, 6, 2, 4, 8, 9, None],
		[4, 8, 7, 9, 5, 3, 1, 6, None]
	])
	assert solve([
		[3   , None, None, 2   , None, 1   , None, None, None],
		[7   , 4   , None, None, None, None, None, 1   , 9   ],
		[None, 2   , None, None, 6   , None, 5   , None, None],
		[None, 3   , None, 7   , 4   , None, None, None, 1   ],
		[None, None, 8   , None, None, None, 9   , None, None],
		[6   , None, None, None, 9   , 2   , None, 5   , None],
		[None, None, 2   , None, 8   , None, None, 4   , None],
		[1   , 5   , None, None, None, None, None, 9   , 7   ],
		[None, None, None, 9   , None, 3   , None, None, 2   ]
	])
