import sys
import itertools

from typing import List, Tuple



def get_abs_differences(*values: int) -> int:
	return sum(abs(value - other) for i, value in enumerate(values) for other in values[i:])


def efficient_solve(*arrays: List[int]) -> Tuple[int, ...]:
	for array in arrays:
		array.sort()

	indexes = [0] * len(arrays)

	smallest = sys.maxsize
	result = tuple()
	while all(indexes[i] < len(array) for i, array in enumerate(arrays)):
		values = [array[indexes[i]] for i, array in enumerate(arrays)]
		if all(value == values[0] for value in values):
			return tuple(values)

		indexes[min(
			range(len(arrays)),
			key = lambda i: values[i]
		)] += 1

		if (diff := get_abs_differences(*values)) < smallest:
			smallest = diff
			result = tuple(values)

	return result


def brute_solve(*arrays: List[int]):
	smallest = sys.maxsize
	result = tuple()

	for product in itertools.product(*arrays):
		if (diff := get_abs_differences(*product)) < smallest:
			smallest = diff
			result = product

	return result


def brute_oneline_solve(*arrays: List[int]) -> Tuple[int, ...]:
	return min(itertools.product(*arrays), key = lambda product: get_abs_differences(*product))


def test_solve():
	for solve in (brute_solve, efficient_solve, brute_oneline_solve):
    assert solve([-1, 3], [3]) == (3, 3)
		assert solve([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]) == (28, 26)
		assert solve([-8, 4, 9, 38, 15, 67], [78, 55, 91, 30, 45, -19]) == (38, 45)
		assert solve([1, 2, 3, 4], [6, 7, 8, 9], [3, 5, 6, 7]) == (4, 6, 5)
