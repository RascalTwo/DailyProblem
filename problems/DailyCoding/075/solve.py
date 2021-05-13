from typing import List



def solve_dp(array: List[int]) -> int:
	longest = [1 for _ in range(len(array))]
	for i in range(1, len(array)):
		for j in range(0, i):
			if array[i] >= array[j]:
				longest[i] = max(longest[i], longest[j] + 1)

	return max(longest)


def solve_recur(numbers: List[int], path: List[int] = []) -> int:
	longest = len(path)

	if not path:
		return max([longest, *[solve_recur(numbers, path + [i]) for i in range(len(numbers))]])

	last_index = path[-1]
	last_value = numbers[last_index]
	return max([longest, *[solve_recur(numbers, path + [i]) for i, value in enumerate(numbers[last_index + 1:], last_index + 1) if value >= last_value]])


def solve_iter(numbers: List[int]) -> int:
	longest = 0

	paths = [[i] for i in range(len(numbers))]
	while paths:
		current = paths.pop()
		longest = max(longest, len(current))

		last_index = current[-1]
		last_value = numbers[last_index]
		paths.extend(current + [i] for i, value in enumerate(numbers[last_index + 1:], last_index + 1) if value >= last_value)

	return longest


def test_solve():
	for solve in (solve_dp, solve_recur, solve_iter):
		assert solve([15, 100, 5, 10, 200]) == 3
		assert solve([5, 4, 3, 2, 1]) == 1
		assert solve([1, 2, 3, 4, 5]) == 5
		assert solve([2, 2, 2]) == 3
		assert solve([4, 6, 3, 7, 9, 12, 1]) == 5
		assert solve([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
