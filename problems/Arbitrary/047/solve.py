from typing import Dict, List, Literal, Set, Tuple, Union



Piece = Union[Literal['>'], Literal['<'], Literal['v'], Literal['^'], Literal['E']]

changes: Dict[Piece, Tuple[int, int]] = {
	'>': (0, 1),
	'<': (0, -1),
	'^': (-1, 0),
	'v': (1, 0),
}


def solve(maze: List[List[Piece]]):
	rows, columns = len(maze), len(maze[0])
	seen: Set[Tuple[int, int]] = set()
	r, c = 0, 0
	while True:
		seen.add((r, c))
		ro, co = changes[maze[r][c]]
		r += ro
		c += co

		if r < 0 or c < 0 or r >= rows or c >= columns:
			return False
		if (r, c) in seen:
			return False
		if maze[r][c] == 'E':
			return True


def test_solve():
	assert solve([['>', '>', '>', '>', 'v'], ['v', '^', '>', '^', 'v'], ['>', '^', '^', '>', 'E']]) == True  # type: ignore
	assert solve([['v', '>', 'v'], ['v', '^', '>'], ['<', '>', 'E']]) == False  # type: ignore
	assert solve([['v', '>', '>', 'v', '>'], ['>', '>', 'v', '>', '^'], ['^', '>', '>', '>', 'E']]) == True  # type: ignore
	assert solve([['v', '>', '>', 'v'], ['v', '^', '>', '>'], ['v', '>', '>', 'v'], ['v', '^', '<', 'v'], ['>', '>', '^', 'E']]) == True  # type: ignore
	assert solve([['>', '>', '>', '>', '>', '>', '>', '>', '>', 'v'], ['v', '^', '>', 'v', '<', '>', 'v', '<', '<', '<'], ['>', '^', 'v', '<', '^', '<', '<', '^', '>', 'E']]) == False  # type: ignore
	assert solve([['>', '>', 'v', 'E', 'v'], ['v', '^', '>', '^', 'v'], ['>', '^', '^', '>', '>']]) == True  # type: ignore
	assert solve([['>', '>', 'v', '>', 'v'], ['v', '^', '>', '^', 'v'], ['>', 'E', '^', '>', '>']]) == False  # type: ignore
	assert solve([['>', '>', 'v', '>', '^'], ['v', '^', '>', '^', 'v'], ['>', 'E', '^', '>', '>']]) == False  # type: ignore
	assert solve([['>', 'v', '>', '>', 'v', '^'], ['v', '<', '^', 'v', '<', 'E'], ['>', '>', '^', '>', '>', '^']]) == True  # type: ignore
	assert solve([['>', 'v', '>', '>', 'v', '^'], ['v', '<', '^', '^', '<', 'E'], ['>', '>', '^', '>', '>', '^']]) == False  # type: ignore

