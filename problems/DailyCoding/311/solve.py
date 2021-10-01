from typing import List



def solve_iter(numbers: List[int]) -> int:
	peak = -1
	best_slope = 0
	for i, number in enumerate(numbers[1:-1], 1):
		left, right = numbers[i - 1], numbers[i + 1]
		if number < left or number < right:
			continue

		slope = (number - left) + (number - right)
		if slope > best_slope:
			peak, best_slope = i, slope

	return peak


def solve_oneline(numbers: List[int]) -> int:
	return max(
		filter(
			lambda item: item[1] > numbers[item[0] - 1] and item[1] > numbers[item[0] + 1],
			enumerate(numbers[1:-1], 1)
		),
		key = lambda item: (item[1] - numbers[item[0] - 1]) + (item[1] - numbers[item[0] + 1]),
		default = (-1, None)
	)[0]


def test_solve():
	for solve in (solve_iter, solve_oneline):
		assert solve([1, 2, 3, 1]) == 2
		assert solve([1, 2, 3, 4]) == -1
		assert solve([8, 7, 6, 1, 4, 5, 3, 9, 8, 4]) == 7
