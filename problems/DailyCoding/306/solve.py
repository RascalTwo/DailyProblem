import heapq

from typing import List



def insertion_sort_solve(array: List[int], k: int) -> List[int]:
	for i, key in enumerate(array):
		j = i - 1
		while j >= 0 and array[j] > key:
			array[j + 1] = array[j]
			j -= 1
		array[j + 1] = key
	return array


def heap_solve(array: List[int], k: int) -> List[int]:
	heap = array[:k + 1]
	heapq.heapify(heap)

	i = k + 1
	for i in range(k + 1, len(array)):
		array[i - (k + 1)] = heapq.heappop(heap)
		heapq.heappush(heap, array[i])

	i += 1
	while heap:
		array[i - (k + 1)] = heapq.heappop(heap)
		i += 1

	return array


def test_solve():
	for solve in (insertion_sort_solve, heap_solve):
		assert solve([2, 1, 3, 5, 4], 1) == [1, 2, 3, 4, 5]
		assert solve([3, 4, 1, 2, 5, 7, 6, 9, 8], 2) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
