from typing import List


def solve(numbers: List[int]) -> int:
	most = 0
	for i in range(len(numbers)):
		for j in range(i + 1, len(numbers) + 1):
			if (sub_sum := sum(numbers[i:j])) > most:
				most = sub_sum
	return most



def test_solve():
	assert solve([34, -50, 42, 14, -5, 86]) == 137
	assert solve([-5, -1, -8, -9]) == 0
