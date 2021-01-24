import copy


from typing import Iterable, List, Optional, Sequence, Set, Tuple



Coordinate = Tuple[int, int]


def calculate_bounds(coords: Sequence[Coordinate], least: Optional[Coordinate] = None, most: Optional[Coordinate] = None) -> Tuple[Coordinate, Coordinate]:
	if not coords:
		return (least if least else (0, 0), most if most else (0, 0))

	first = next(iter(coords))
	least = least if least else copy.deepcopy(first)
	most = most if most else copy.deepcopy(first)

	for (x, y) in coords:
		if x < least[0]:
			least = (x, least[1])
		if y < least[1]:
			least = (least[0], y)
		if x > most[0]:
			most = (x, most[1])
		if y > most[1]:
			most = (most[0], y)

	return least, most


def test_calculate_bounds():
	assert calculate_bounds([]) == ((0, 0), (0, 0))
	assert calculate_bounds([], (1, 5), (5, 1)) == ((1, 5), (5, 1))
	assert calculate_bounds([(-2, 1), (0, 0), (3, 4)]) == ((-2, 0), (3, 4))


def to_board(living_cells: Sequence[Coordinate], least: Optional[Coordinate] = None, most: Optional[Coordinate] = None) -> Tuple[Tuple[Optional[Coordinate], Optional[Coordinate]], List[List[str]]]:
	if not living_cells:
		return ((least, most), [])

	if not least or not most:
		least, most = calculate_bounds(living_cells)

	return (
		(least, most),
		[
			['*' if (x, y) in living_cells else '.' for y in range(least[1], most[1] + 1)]
			for x in range(least[0], most[0] + 1)
		]
	)


def test_to_board():
	assert to_board([(0, 0), (-2, -2), (2, 2)]) == (
		((-2, -2), (2, 2)),
		[
			['*', '.', '.', '.', '.'],
			['.', '.', '.', '.', '.'],
			['.', '.', '*', '.', '.'],
			['.', '.', '.', '.', '.'],
			['.', '.', '.', '.', '*']
		]
	)

def generate_board_string(board: List[List[str]]) -> Iterable[str]:
	for row in board:
		for cell in row:
			yield cell + ' '
		yield '\n'


def generate_board_strings(cell_states: Sequence[Sequence[Coordinate]]) -> Iterable[str]:
	least_least = None
	most_most = None
	for cells in cell_states:
		least, most = calculate_bounds(cells)

		least_least = (min(least_least[0], least[0]), min(least_least[1], least[1])) if least_least else least
		most_most = (max(most_most[0], most[0]), max(most_most[1], most[1])) if most_most else most

	yield from (''.join(generate_board_string(to_board(cells, least_least, most_most)[1])) for cells in cell_states)


def solve(initial_cells: Sequence[Coordinate], steps: int) -> Iterable[Sequence[Coordinate]]:
	live_cells = initial_cells[:]
	least, most = calculate_bounds(initial_cells)
	for _ in range(steps):
		new_cells: Set[Coordinate] = set()

		for x in range(least[0] - 1, most[0] + 2):
			for y in range(least[1] - 1, most[1] + 2):
				living_neighbors = sum((x + xo, y + yo) in live_cells for xo, yo in ((1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)))

				living = (x, y) in live_cells
				if (living and living_neighbors in (2, 3)) or (not living and living_neighbors == 3):
					new_cells.add((x, y))

		least, most = calculate_bounds(new_cells, least, most)
		live_cells = new_cells

		yield new_cells


def test_solve():
	assert list(generate_board_strings(list(solve([(0, -1), (0, 0), (0, 1)], 3)))) == ['. * . \n. * . \n. * . \n', '. . . \n* * * \n. . . \n', '. * . \n. * . \n. * . \n']
