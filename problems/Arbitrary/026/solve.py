from typing import List



def find_missing_set(first: List[int], second: List[int]):
	return next(iter(set(first) - set(second)))


def find_missing_math(first: List[int], second: List[int]):
	return sum(first) - sum(second)


def find_missing_iter(first: List[int], second: List[int]):
	return next(num for num in first if num not in second)


def test_solve():
	for solve in (find_missing_set, find_missing_math, find_missing_iter):
		assert solve([1, 5, 3, 8], [8, 5, 1]) == 3
		assert solve([7, -4, 98, -34], [-4, 98, 7]) == -34
