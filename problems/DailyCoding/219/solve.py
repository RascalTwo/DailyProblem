import unittest.mock

import os

from typing import Any, List, Optional, Tuple



class ConnectN:
	def __init__(self, n: int = 4, width: int = 7, height: int = 6):
		self.n = n
		self.width = width
		self.height = height

		self.board: List[List[Optional[int]]] = []
		self.winning_pieces: List[Tuple[Tuple[int, int], ...]] = []
		self.game_over = False
		self.reset()

	def reset(self):
		self.board = [[None for _ in range(self.height)] for _ in range(self.width)]
		self.winning_pieces = []
		self.game_over = False

	def can_place(self, column: int):
		return self.board[column][-1] is None

	def move(self, piece: int, column: int) -> Optional[int]:
		if not self.can_place(column) or self.game_over:
			return

		for row, value in enumerate(self.board[column]):
			if value is None:
				self.board[column][row] = piece
				self.calculate_winning_pieces(column, row)
				return row

	def calculate_winning_pieces(self, column: int, row: int):
		piece = self.board[column][row]
		offsets = [(0, -1), (-1, 0), (-1, -1)]
		for col_offset, row_offset in offsets:
			least_col = column
			least_row = row
			while least_col >= 0 and least_row >= 0:
				next_col, next_row = least_col + col_offset, least_row + row_offset
				if self.board[next_col][next_row] != piece:
					break
				least_col, least_row = next_col, next_row

			locations: List[Tuple[int, int]] = []
			for i in range(self.n):
				next_col, next_row = least_col + (-col_offset * i), least_row + (-row_offset * i)
				if next_col >= self.height - 1 or next_row >= self.width - 1 or self.board[next_col][next_row] != piece:
					break
				locations.append((next_col, next_row))
			else:
				self.winning_pieces.append(tuple(locations))

		if self.winning_pieces:
			self.game_over = True

		if not any(any(value is None for value in row) for row in self.board):
			self.game_over = True


def test_connect_n():
	connect = ConnectN()
	assert not connect.game_over

	connect.move(1, 0)
	connect.move(1, 0)
	connect.move(1, 0)
	connect.move(1, 0)
	assert connect.game_over and connect.winning_pieces[0][0] == (0, 0)

	connect.reset()
	assert not connect.game_over

	connect = ConnectN(2)
	connect.move(1, 0)
	connect.move(9, 1)
	connect.move(1, 1)
	assert connect.game_over

	connect = ConnectN()
	connect.move(1, 0)
	connect.move(1, 1)
	connect.move(1, 2)
	connect.move(1, 3)
	assert connect.move(1, 0) is None
	assert connect.game_over

	connect = ConnectN(4, 2, 2)
	connect.move(0, 0)
	connect.move(0, 0)
	connect.move(0, 1)
	connect.move(0, 1)
	assert connect.game_over


class ConnectNCLI(ConnectN):
	def __init__(self, *args: Any):
		super().__init__(*args)

	def piece_to_str(self, piece: Optional[int]):
		return str(piece) if piece is not None else ' '

	def __str__(self):
		lines: List[str] = [
			'┌' + ('─┬' * (self.width - 1)) + '─┐'
		]
		for row in range(self.height):
			pieces: List[str] = []
			for column in range(self.width):
				pieces.append(self.piece_to_str(self.board[column][-row + -1]))
			lines.append('│' + '│'.join(pieces) + '│')
			lines.append('├' + ('─┼' * (self.width - 1)) + '─┤')

		lines[-1] = '└' + ('─┴' * (self.width - 1)) + '─┘'
		return '\n'.join(lines)

	def start(self):
		pieces: List[int] = [1, 2]
		piece_index = 0
		while not self.game_over:
			try:
				print(str(self))
				column = int(input(f'Column (1 - {self.width}): '))
				if column < 1 or column > self.width:
					raise ValueError
			except ValueError:
				print(f'Invalid column number')
				continue
			row = self.move(pieces[piece_index], column - 1)
			if row is None:
				print('Column is full')
				continue
			piece_index = (piece_index + 1) % len(pieces)
			os.system('cls' if os.name == 'nt' else 'clear')

		if self.winning_pieces:
			column, row = self.winning_pieces[0][0]
			print(f'{self.board[column][row]} won!')
		else:
			print('Tie')

def test_connect_n_cli():
	with unittest.mock.patch('builtins.input', side_effect=['1', '2' ,'1', '2', '1', '2', '1']):
		with unittest.mock.patch('builtins.print'):
			with unittest.mock.patch('os.system'):
				connect = ConnectNCLI()
				connect.start()
				assert connect.game_over and connect.winning_pieces and connect.winning_pieces[0][0] == (0, 0)
