from typing import List



def solve(digits: List[int]) -> List[int]:
	carrying = False
	for i in range(len(digits) - 1, -1, -1):
		digits[i] += 1
		carrying = digits[i] >= 10
		if carrying:
			digits[i] = 0
		else:
			return digits
	if carrying:
		digits.insert(0, 1)
	return digits


def test_solve():
	assert solve([1, 2, 3]) == [1, 2, 4]
	assert solve([4, 3, 2, 1]) == [4, 3, 2, 2]
	assert solve([9]) == [1, 0]
