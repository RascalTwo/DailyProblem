from typing import List



def solve_native(array: List[int], k: int, smallest: bool) -> int:
	array = array[:]
	array.sort(reverse=not smallest)
	return array[k]


def solve_bubble(array: List[int], k: int, smallest: bool) -> int:
	array = array[:]

	for i in range(k + 1):
		for j in range(0, len(array) - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]

	return array[k if smallest else len(array) - 1 - k]


def test_solve():
	for solve in (solve_native, solve_bubble):
		for arr in ([4, 2, 8, 3, 5], ):
			smalls = sorted(arr)
			for i in range(len(smalls)):
				assert solve(arr, i, True) == smalls[i]
			bigs = sorted(arr, reverse=True)
			for i in range(len(bigs)):
				assert solve(arr, i, False) == bigs[i]
