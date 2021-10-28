import itertools

from typing import Dict, List, Optional, Tuple



def solve_iter(numbers: List[int], target: int) -> Optional[Tuple[int, int, int]]:
	for i in range(len(numbers) - 2):
		for j in range(i + 1, len(numbers) - 1):
			for k in range(j + 1, len(numbers)):
				if numbers[i] + numbers[j] + numbers[k] == target:
					return numbers[i], numbers[j], numbers[k]


def solve_itertools(numbers: List[int], target: int):
	for combo in itertools.combinations(numbers, 3):
		if sum(combo) == target:
			return combo


def solve_map(numbers: List[int], target: int):
	complements: Dict[int, Tuple[int, int]] = {}
	for i, first in enumerate(numbers[:-2]):
		for j, second in enumerate(numbers[i:-1], 1):
			complements[target - (first + second)] = (first, second)
			for third in numbers[j:]:
				if third in complements:
					return (*complements[third], third)


def solve_pointers(numbers: List[int], target: int):
	numbers.sort()
	for i, a in enumerate(numbers):
		goal = target - a

		left = i + 1
		right = len(numbers) - 1

		while left < right:
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
		assert solve([-4, 5, 2], 0) is None
		assert solve([1, 2, 3, 4], 9) == (2, 3, 4)
		assert solve([1, 5, 4, 2, 3, 6, 9, 7, 8, 10], 20) == (1, 9, 10)
		assert solve([-1, 0, 1, 2, -1, -4], 0) in [(-1, 0, 1), (-1, -1, 2)]