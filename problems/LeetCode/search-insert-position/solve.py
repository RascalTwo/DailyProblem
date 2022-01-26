from typing import List



def solve(nums: List[int], target: int) -> int:
	left, right = 0, len(nums)
	while True:
		middle = (left + right) // 2
		number = nums[middle]
		if number == target or middle in (left, right):
			return middle + int(number != target and number < target)
		if number > target:
			right -= 1
		elif number < target:
			left += 1


def test_solve():
	assert solve([1, 3, 5, 6], 5) == 2
	assert solve([1, 3, 5, 6], 2) == 1
	assert solve([1, 3, 5, 6], 7) == 4
	assert solve([1, 3, 5, 6], 0) == 0
