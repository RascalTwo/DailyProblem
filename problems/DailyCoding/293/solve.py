import sys

from typing import List, Optional, Tuple

def is_pyramid(heights: List[int]) -> bool:
	start = 0
	end = len(heights) - 1
	while heights[start] == 0 and start < len(heights):
		start += 1
	while heights[end] == 0 and end > 0:
		end -= 1

	if heights[start] != 1 or heights[end] != 1:
		return False

	increasing = True
	last_height = 0
	for height in heights[start:end + 1]:
		if last_height == 0 and height == 0:
			continue
		if height == last_height or abs(height - last_height) != 1:
			return False

		if last_height > height and increasing:
			increasing = False

		if (increasing and last_height > height) or (not increasing and last_height < height):
			return False

		last_height = height

	return True

def test_is_pyramid():
	assert is_pyramid([1, 2, 1]) is True
	assert is_pyramid([0, 0, 1, 2, 1, 0, 0]) is True
	assert is_pyramid([1, 2, 2]) is False
	assert is_pyramid([1, 2, 1, 2, 1]) is False
	assert is_pyramid([0, 1, 2, 3, 2, 1]) is True
	assert is_pyramid([1, 1, 3, 3, 2, 1]) is False

def recur_until_pyramid(heights: List[int]) -> Tuple[Optional[List[int]], int]:
	if is_pyramid(heights):
		return heights, 0

	best = (None, sys.maxsize)

	top_index = max(range(len(heights)), key = lambda i: heights[i])

	for i, height in enumerate(heights[:-1]):
		if height != heights[i + 1]:
			continue

		m = i if i < top_index else i + 1
		pyramid, cost = recur_until_pyramid(heights[:m] + [heights[m] - 1] + heights[m + 1:])
		if cost < best[1]:
			best = pyramid, cost

	return best[0], best[1] + 1


def solve(initial_heights: List[int]) -> Tuple[Optional[List[int]], int]:
	tops: List[int] = []
	tallest = max(initial_heights)
	for i, height in enumerate(initial_heights):
		if height == tallest:
			tops.append(i)

	best = (None, sys.maxsize)
	for top in tops:
		heights = initial_heights[:]
		changes = 0
		while True:
			for other in tops:
				if top != other:
					heights[other] -= 1
					changes += 1

			height = heights[top]
			if height - top <= 1 and height - (len(heights)-1-top) <= 1:
				break

			heights[top] -= 1
			changes += 1

		pyramid, cost = recur_until_pyramid(heights)
		if cost < best[1]:
			best = pyramid, cost + changes

	return best[0], best[1]


def test_solve():
	assert solve([1, 1, 3, 3, 2, 1]) == ([0, 1, 2, 3, 2, 1], 2)
	assert solve([0, 1, 1, 3, 3, 2, 1, 0]) == ([0, 0, 1, 2, 3, 2, 1, 0], 2)
	assert solve([1, 2, 1, 2]) == ([1, 2, 1, 0], 2)
	assert solve([2, 2, 3, 2, 2]) == ([1, 2, 3, 2, 1], 2)
	assert solve([2, 2, 4, 2, 2]) == ([1, 2, 3, 2, 1], 3)
	assert solve([2, 2, 6, 6, 2, 2]) == ([0, 1, 2, 3, 2, 1], 11)