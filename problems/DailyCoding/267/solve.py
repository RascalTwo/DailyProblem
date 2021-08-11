import enum
import sys


from typing import Iterable, List, Optional, Set, Tuple

Location = Tuple[int, int]



class Piece(enum.Enum):
	King = 'K'
	Queen = 'Q'
	Pawn = 'P'
	Bishop = 'B'
	Knight = 'N'
	Rook = 'R'
	Empty = '.'


	@classmethod
	def from_str(cls, string: str) -> 'Piece':
		return cls(string)


Board = List[List[Piece]]


def _get_linear_destinations(board: Board, location: Location, offsets: Iterable[Location], distance: int = sys.maxsize) -> Iterable[Location]:
	for offset in offsets:
		current = location
		for _ in range(distance):
			current = current[0] + offset[0], current[1] + offset[1]
			if 0 <= current[0] < len(board) and 0 <= current[1] < len(board[current[0]]):
				yield current
			else:
				break
			dest_piece = board[current[0]][current[1]]
			if dest_piece != Piece.Empty:
				break


def _get_straight_destinations(board: Board, location: Location, distance: int = sys.maxsize) -> Iterable[Location]:
	return _get_linear_destinations(board, location, ((0, 1), (0, -1), (1, 0), (-1, 0)), distance)


def _get_diagonal_destination(board: Board, location: Location, distance: int = sys.maxsize) -> Iterable[Location]:
	return _get_linear_destinations(board, location, ((1, 1), (-1, -1), (1, -1), (-1, 1)), distance)


def get_destinations(board: Board, piece: Piece, location: Location) -> Iterable[Location]:
	if piece == Piece.King:
		yield from _get_straight_destinations(board, location, 1)
		yield from _get_diagonal_destination(board, location, 1)
	elif piece == Piece.Queen:
		yield from _get_straight_destinations(board, location)
		yield from _get_diagonal_destination(board, location)
	elif piece == Piece.Rook:
		yield from _get_straight_destinations(board, location)
	elif piece == Piece.Bishop:
		yield from _get_diagonal_destination(board, location)
	elif piece == Piece.Pawn:
		yield from _get_linear_destinations(board, location, [(-1, 0)], 2 if location[0] == len(board) - 2 else 1)
	elif piece == Piece.Knight:
		yield from _get_linear_destinations(board, location, [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)], 1)


def parse_raw_board(raw_board: str) -> Board:
	board: Board = []
	for line in (line.strip() for line in raw_board.split('\n')):
		if not line:
			continue
		board.append([Piece.from_str(char) for char in line])
	return board


def solve(raw_board: str) -> bool:
	board = parse_raw_board(raw_board)
	white_destinations: Set[Location] = set()
	king_loc: Optional[Location] = None
	for x, row in enumerate(board):
		for y, piece in enumerate(row):
			if piece == Piece.Empty:
				continue

			if piece == Piece.King:
				king_loc = x, y
				continue

			if king_loc is None:
				white_destinations |= set(get_destinations(board, piece, (x, y)))
				continue

			if any(dest == king_loc for dest in get_destinations(board, piece, (x, y))):
				return True

			if not white_destinations:
				continue
			if any(dest == king_loc for dest in white_destinations):
				return True
			white_destinations.clear()

	return False


def test_solve():
	assert solve('''
		...K....
		........
		.B......
		......P.
		.......R
		..N.....
		........
		.....Q..
	''') is True
	assert solve('''
		...K....
		........
		........
		......P.
		.......R
		..N.....
		........
		.....Q..
	''') is False
	assert solve('''
		...K....
		...P....
		........
	''') is True
	assert solve('''
		...K....
		........
		...P....
		........
	''') is True
	assert solve('''
		...K....
		........
		....N...
	''') is True
	assert solve('''
		...K....
		.....N..
	''') is True
