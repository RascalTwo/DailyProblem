import random


from typing import List, Tuple



OFFSETS: List[Tuple[int, int]] = [
	(2, 1), (2, -1), (-2, 1), (-2, -1),
	(1, 2), (-1, 2), (1, -2), (-1, -2)
]


def solve(k: int):
	position: Tuple[int, int] = random.randint(0, 7), random.randint(0, 7)
	off_board_moves = 0
	for _ in range(k):
		offset: Tuple[int, int] = random.choice(OFFSETS)
		new_position: Tuple[int, int] = position[0] + offset[0], position[1] + offset[1]
		if all(0 <= coord < 8 for coord in new_position):
			position = new_position
		else:
			off_board_moves += 1
	return off_board_moves / k


def test_solve():
	print(solve(1000000))
