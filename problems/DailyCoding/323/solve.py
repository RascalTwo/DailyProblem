import heapq
import math

from typing import List



def solve(numbers: List[int]) -> float:
	length = 0
	heap: List[int] = []
	for number in numbers:
		heapq.heappush(heap, number)
		length += 1

	medians: List[int] = []
	middle_indexes = sorted(set([math.floor(length / 2), math.ceil(length / 2)]), reverse=True)
	for i in range(length):
		value = heapq.heappop(heap)
		if middle_indexes[-1] == i:
			medians.append(value)
		if not middle_indexes:
			break

	return sum(medians) / len(medians)


def test_solve():
	assert solve([1, 10, 6, 15, 12, 2, 5, 7, 8, 9, 11, 3, 4, 14, 38, 45, 16, 95, 789]) == 10
