from typing import List, Tuple



def solve_iter(numbers: List[int]) -> Tuple[int, int]:
	least = numbers[0]
	most = numbers[0]
	for number in numbers:
		if number < least:
			least = number
		elif number > most:
			most = number
	return least, most


def solve_recur(numbers: List[int]) -> Tuple[int, int]:
	count = len(numbers)
	if count == 1:
		return numbers[0], numbers[0]
	if count == 2:
		return (numbers[0], numbers[1]) if numbers[0] < numbers[1] else (numbers[1], numbers[0])

	middle = count // 2
	left = solve_recur(numbers[middle:])
	right = solve_recur(numbers[:middle])

	return min(left[0], right[0]), max(left[1], right[1])


def test_solve():
	for solve in (solve_iter, solve_recur):
		assert solve([1, 3, 5, 7, 2, 1, 45, 765, 8, 24, 21]) == (1, 765)
