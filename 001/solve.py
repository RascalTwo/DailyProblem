import itertools

from typing import List



def solve_itertools(numbers: List[int], k: int, length: int = 2) -> bool:
	return any(sum(combo) == k for combo in itertools.combinations(numbers, length))


def solve_iter(numbers: List[int], k: int) -> bool:
	for i in range(len(numbers) - 1):
		for j in range(i + 1, len(numbers)):
			if numbers[i] + numbers[j] == k:
				return True

	return False


def solve_map(numbers: List[int], k: int) -> bool:
	others = {}
	for num in numbers:
		other = k - num
		if other in others:
			return True
		others[num] = other

	return False

def solve_sorted_pointers(numbers: List[int], k: int) -> bool:
	numbers.sort()
	i = 0
	j = len(numbers) - 1
	while i < j:
		a, b = numbers[i], numbers[j]
		total = a + b
		if total == k:
			return True
		if total > k:
			if a < b:
				j -= 1
			else:
				i += 1
		else:
			if a < b:
				i += 1
			else:
				j -= 1

	return False


def test_solve():
	for solve in [solve_itertools, solve_map, solve_sorted_pointers, solve_iter]:
		assert solve([10, 15, 3, 7], 17) is True
		assert solve([9, 4, 3, 6], 39) is False
		assert solve([7, 3, 15, 10], 17) is True
		assert solve([1, 2], 3) is True
		assert solve([1], 3) is False
		assert solve([1, 4, 9, 6], 10) is True

test_solve()
