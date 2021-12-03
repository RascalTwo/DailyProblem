from typing import List, Tuple



def solve(numbers: List[int]) -> List[int]:
	numbers.sort()
	best: Tuple[int, int] = (0, 1)
	i = 0
	j = 1
	def update_best():
		nonlocal best, i, j
		length = j - i
		if length > best[1]:
			best = (i, length)
		i = j
		j += 1

	while i < len(numbers) and j < len(numbers):
		if numbers[j] - numbers[j - 1] == 1:
			j += 1
		else:
			update_best()
	update_best()

	return numbers[best[0]: sum(best)]


def test_solve():
	assert solve([5, 2, 99, 3, 4, 1, 100]) == [1, 2, 3, 4, 5]
