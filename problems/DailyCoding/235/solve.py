from typing import List, Tuple



def solve(numbers: List[int]) -> Tuple[int, int]:
	least = numbers[0]
	most = numbers[0]
	for number in numbers:
		if number < least:
			least = number
		elif number > most:
			most = number
	return least, most


def test_solve():
	assert solve([1, 3, 5, 7, 2, 1, 45, 765, 8, 24, 21]) == (1, 765)
