from typing import List, Tuple



def solve_plain(lst: List[int]) -> Tuple[int, int]:
	best = ((0, 0), 0)
	for left in range(len(lst) - 1):
		for right in range(left + 1, len(lst)):
			area = min(lst[left], lst[right]) * (right - left)
			if area > best[1]:
				best = ((left, right), area)

	return best[0]


def solve_optimal(lst: List[int]) -> Tuple[int, int]:
	left = 0
	right = len(lst) - 1
	best = ((left, right), 0)

	while left < right:
		area = min(lst[left], lst[right]) * (right - left)
		if area > best[1]:
			best = ((left, right), area)

		if lst[left] < lst[right]:
			left += 1
		else:
			right -= 1

	return best[0]


def test_solve():
	for solve in (solve_plain, solve_optimal):
		assert solve([1, 8, 6, 2, 5, 4, 8, 3, 7]) == (1, 8)
		assert solve([1, 1]) == (0, 1)
		assert solve([4, 3, 2, 1, 4]) == (0, 4)
		assert solve([1, 2, 1]) == (0, 2)
