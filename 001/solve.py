import itertools

from typing import List



def solve_itertools(numbers: List[int], k: int, length: int = 2) -> bool:
	return any(sum(combo) == k for combo in itertools.combinations(numbers, length))


def solve_map(numbers: List[int], k: int) -> bool:
	others = {}
	for num in numbers:
		other = k - num
		if other in others:
			return True
		others[num] = other

	return False


def test_solve():
	for solve in [solve_itertools, solve_map]:
		assert solve([10, 15, 3, 7], 17)
		assert solve([9, 4, 3, 6], 39) is False
		assert solve([7, 3, 15, 10], 17)

