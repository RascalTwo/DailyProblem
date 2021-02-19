from typing import List



def is_prime(num: int) -> bool:
	for i in range(2, int((num / 2) + 1)):
		if not num % i:
			return False

	return num > 1


def solve(integers: List[int]) -> int:
	return sum(is_prime(num) for num in integers)


def test_solve():
	assert solve([1, 2, 3]) == 2
	assert solve([17]) == 1
	assert solve([4, 6, 8, 10]) == 0
	assert solve([4, 4, 4, 13, 4, 4, 4]) == 1
	assert solve([4, 8, 6, 2, 75, 98, 35, 14, 43, 48]) == 2
