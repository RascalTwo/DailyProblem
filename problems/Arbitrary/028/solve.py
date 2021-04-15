import itertools

from typing import Dict, List, Optional, Tuple



def solve_iter(numbers: List[int], target: int) -> Optional[Tuple[int, int, int]]:
	for first in numbers:
		for second in numbers:
			for third in numbers:
				if first + second + third == target:
					return first, second, third


def solve_itertools(numbers: List[int], target: int):
	for combo in itertools.product(numbers, repeat=3):
		if sum(combo) == target:
			return combo


def solve_map(numbers: List[int], target: int) -> Optional[Tuple[int, int, int]]:
	complements: Dict[int, Tuple[int, int]] = {}
	for first in numbers:
		for second in numbers:
			complements[target - (first + second)] = (first, second)
			for third in numbers:
				if third in complements:
					return (*complements[third], third)


def solve_pointers(numbers: List[int], target: int):
	numbers.sort()
	for a in numbers:
		goal = target - a

		left = 0
		right = len(numbers) - 1

		while not left > right:
			b, c = numbers[left], numbers[right]
			total = b + c
			if total == goal:
				return a, b, c
			if total > goal:
				right -= 1
			else:
				left += 1


def test_solve():
	for solve in (solve_iter, solve_itertools, solve_map, solve_pointers):
		assert solve([-4, 5, 2], 0) == (-4, 2, 2)
		assert solve([1, 2, -4, 4], 9) == (1, 4, 4)
		assert solve([1, 5, 4, 8, 10], 20) in [(4, 8, 8), (5, 5, 10)]
		assert solve([-2, 1], 0) == (-2, 1, 1)
