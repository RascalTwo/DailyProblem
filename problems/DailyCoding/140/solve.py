import collections


from typing import List, Set



def solve_counter(integers: List[int]) -> List[int]:
	return [key for key, value in collections.Counter(integers).items() if value == 1]


def solve_set(integers: List[int]) -> List[int]:
	seen: Set[int] = set()

	for value in integers:
		getattr(seen, 'remove' if value in seen else 'add')(value)

	return list(seen)


def test_solve():
	for solve in (solve_counter, solve_set):
		assert solve([2, 4, 6, 8, 10, 2, 6, 10]) == [4, 8]
