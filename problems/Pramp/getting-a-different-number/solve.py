from typing import List



def solve_hashed(arr: List[int]) -> int:
	seen = set(arr)
	result = 0
	while result in seen:
		result += 1
	return result


def solve_sorted(arr: List[int]) -> int:
	sorted_arr = sorted(arr)
	for i, value in enumerate(sorted_arr):
		if i != value:
			return i

	return len(sorted_arr)


def solve_efficient_sorted(arr: List[int]) -> int:
	for i, value in enumerate(arr):
		while value < len(arr) and arr[value] != value:
			temp = arr[value]
			arr[value] = value
			value = temp

	for i, value in enumerate(arr):
		if i != value:
			return i

	return len(arr)


def test_solve():
	for solve in (solve_hashed, solve_sorted, solve_efficient_sorted):
		assert solve([0]) ==  1
		assert solve([0, 1, 2]) ==  3
		assert solve([1, 3, 0, 2]) ==  4
		assert solve([1000000]) ==  0
		assert solve([1, 0, 3, 4, 5]) ==  2
		assert solve([0, 1000000]) ==  1
		assert solve([0, 99999, 1000000]) ==  1
		assert solve([0, 5, 4, 1, 3, 6, 2]) ==  7