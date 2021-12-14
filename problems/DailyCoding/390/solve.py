import random

from typing import List, Set



def solve(integers: List[int], low: int, high: int) -> Set[int]:
	found = {i: False for i in range(low, high)}
	for i in integers:
		found[i] = True

	return set(i for i in found if not found[i])


def test_solve():
	def assert_solve(low: int, high: int, removing: int):
		integers = list(range(low, high))
		missing = set(integers.pop(value) for value in sorted(random.choices(integers, k=removing), reverse=True))
		assert solve(integers, low, high) == missing

	assert_solve(1, 11, 3)
	assert_solve(1, 1000001, 1000)