import itertools

from typing import Iterable, Set



def generate_perfect_squares(max: int) -> Iterable[int]:
	i = 1
	while True:
		square = i * i
		if square > max:
			return
		yield square
		i += 1


def solve(n: int) -> Iterable[Set[int]]:
	squares = list(generate_perfect_squares(n))
	for r in range(1, len(squares)):
		for combo in itertools.combinations_with_replacement(squares, r):
			if sum(combo) == n:
				yield sorted(combo, reverse=True)


def test_solve():
	assert list(solve(4)) == [[4]]
	assert list(solve(16)) == [[16]]
	assert list(solve(17)) == [[16, 1], [9, 4, 4]]
	assert list(solve(18)) == [[9, 9], [16, 1, 1]]
	assert list(solve(25)) == [[25], [16, 9], [16, 4, 4, 1]]
