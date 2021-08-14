from typing import List, Tuple



def solve(integers: List[int]):
	goal = sorted(integers)

	best_window: Tuple[int, int] = (0, len(integers) - 1)
	for i in range(len(integers) - 1):
		for j in range(i + 1, len(integers)):
			sorted_window = sorted(integers[i:j + 1])
			if integers[i:j + 1] == sorted_window:
				continue

			partial_sorted = integers[:]
			partial_sorted[i:j + 1] = sorted_window
			if partial_sorted == goal and j - i < best_window[1] - best_window[0]:
				best_window = i, j

	return best_window


def test_solve():
	assert solve([3, 7, 5, 6, 9]) == (1, 3)
	assert solve([9, 8, 7, 6, 5, 4]) == (0, 5)
	assert solve([1, 2, 3, 5, 4, 6, 8, 7, 9]) == (3, 7)
