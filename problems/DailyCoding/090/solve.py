import random

from typing import List



def solve(n: int, l: List[int]):
	options = list(set(range(n)) - set(l))
	return lambda: random.choice(options)


def test_solve():
	def assert_solve(n: int, *l: int):
		generate = solve(n, list(l))
		values = [generate() for _ in range(1000000)]
		assert not (set(values) & set(l))
	assert_solve(10, 1, 3, 7)
