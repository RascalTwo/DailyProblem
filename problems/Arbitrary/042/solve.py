from typing import List, Optional, Set



def solve_iter(numbers: List[int]) -> Optional[int]:
	for pivot in range(1, len(numbers) - 1):
		if sum(numbers[:pivot]) == sum(numbers[pivot + 1:]):
			return pivot


def solve_center_iter(numbers: List[int]) -> Optional[int]:
	tried: Set[int] = set()
	pivot = len(numbers) // 2
	while pivot not in tried:
		tried.add(pivot)
		diff = sum(numbers[:pivot]) - sum(numbers[pivot + 1:])
		if not diff:
			return pivot
		elif diff > 0:
			pivot -= 1
		else:
			pivot += 1


def solve_center_iter_sliceless(numbers: List[int]) -> Optional[int]:
	tried: Set[int] = set()
	pivot = len(numbers) // 2
	left = numbers[:pivot]
	right = numbers[pivot + 1:]
	while pivot not in tried:
		tried.add(pivot)
		diff = sum(left) - sum(right)
		if not diff:
			return pivot
		elif diff < 0:
			left.append(numbers[pivot])
			right.pop(0)
			pivot += 1
		else:
			right.append(numbers[pivot])
			left.pop()
			pivot -= 1


def solve_center_iter_listless(numbers: List[int]) -> Optional[int]:
	tried: Set[int] = set()
	pivot = len(numbers) // 2
	lsum = sum(numbers[:pivot])
	rsum = sum(numbers[pivot + 1:])
	while pivot not in tried:
		tried.add(pivot)
		if lsum == rsum:
			return pivot
		elif lsum < rsum:
			lsum += numbers[pivot]
			pivot += 1
			rsum -= numbers[pivot]
		elif lsum > rsum:
			rsum += numbers[pivot]
			pivot -= 1
			lsum -= numbers[pivot]


def solve_center_iter_diff_only(numbers: List[int]) -> Optional[int]:
	tried: Set[int] = set()
	pivot = len(numbers) // 2
	diff = sum(numbers[:pivot]) - sum(numbers[pivot + 1:])
	while pivot not in tried:
		tried.add(pivot)
		if not diff:
			return pivot
		elif diff < 0:
			diff += numbers[pivot] - -numbers[pivot + 1]
			pivot += 1
		else:
			diff += -numbers[pivot - 1] - numbers[pivot]
			pivot -= 1


def solve_two_pointer(numbers: List[int]) -> Optional[int]:
	l = 0
	lsum = 0

	r = len(numbers) - 1
	rsum = 0

	while l < r:
		lsum += numbers[l]
		rsum += numbers[r]
		while lsum != rsum and l < r:
			if lsum < rsum:
				l += 1
				lsum += numbers[l]
			if rsum < lsum:
				r -= 1
				rsum += numbers[r]
		l += 1
		r -= 1

	if lsum == rsum and l == r:
		return l


def solve_two_pointer_diff(numbers: List[int]) -> Optional[int]:
	l = 0
	r = len(numbers) - 1

	diff = 0
	while l < r:
		diff += numbers[l] - numbers[r]

		while diff and l < r:
			if diff < 0:
				l += 1
				diff += numbers[l]
			elif diff > 0:
				r -= 1
				diff -= numbers[r]

		l += 1
		r -= 1

	if not diff and l == r:
		return l


def test_solve():
	for solve in (solve_iter, solve_center_iter, solve_center_iter_sliceless, solve_center_iter_listless, solve_center_iter_diff_only, solve_two_pointer, solve_two_pointer_diff):
		assert solve([1, 2, 3, 3]) == 2
		assert solve([3, 1, 2, 1]) == 1
		assert solve([3, 1, 3, 1]) is None
		assert solve([10, 4, 9, 1]) == 1
		assert solve([10, 4, 1, 9, 1, 3, 1]) == 2
		assert solve([10, 10, 10, 10, 10, 9, 50]) == 5
		assert solve([14, 13, 17, 13, 9, 18, 17, 20, 14, 13, 2, 15, 8, 2, 20, 14, 19, 16, 2, 10]) == 8
		assert solve([13, 2, 8, 14, 15, 10, 3, 16, 8, 15, 12, 20, 15, 16, 1, 7, 5, 20, 12, 8]) == 10
		assert solve([40, 40, 39, 36, 31, 26, 25, 25, 23, 22, 20, 19, 16, 16, 15, 14, 14, 13, 13, 13, 12, 12, 12, 12, 11, 11, 11, 10, 10, 9, 9, 7, 6, 6, 6, 5, 5, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0]) == 10
		assert solve([0, 1, 0, 3, 0, 5, 0, 2, 0, 7, 8, 7, 0, 0, 3, 11, 4, 17, 16, 6, 19, 8, 0, 10, 22, 8, 12, 9, 21, 19, 28, 8, 3, 9, 18, 34, 29, 31, 29, 38, 38, 22, 42, 36, 19, 31, 33, 42, 37, 40]) == 38
