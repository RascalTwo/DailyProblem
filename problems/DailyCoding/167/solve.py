from typing import Iterable, List, Tuple



def solve(words: List[str]) -> Iterable[Tuple[int, int]]:
	for i, first in enumerate(words):
		for j, second in enumerate(words):
			if i == j:
				continue
			if first + second == (first + second)[::-1]:
				yield i, j


def test_solve():
	assert list(solve(["code", "edoc", "da", "d"])) == [(0, 1), (1, 0), (2, 3)]
