from typing import List, Tuple



def solve(nums: List[int], target: int) -> Tuple[int, int]:
	if not nums:
		return -1, -1

	length = len(nums)

	start, end = -1, -1
	left, right = 0, length
	while True:
		middle = (left + right) // 2
		number = nums[middle]
		if number == target:
			start, end = middle, middle
			while start and nums[start - 1] == target:
				start -= 1
			while end + 1 < length and nums[end + 1] == target:
				end += 1
			return start, end

		if middle in (left, right):
			return -1, -1
		elif nums[middle] < target:
			left = middle
		elif nums[middle] > target:
			right = middle



def test_solve():
	assert solve([5, 7, 7, 8, 8, 10], 8) == (3, 4)
	assert solve([5, 7, 7, 8, 8, 10], 6) == (-1, -1)
	assert solve([], 0) == (-1, -1)
	assert solve([1], 1) == (0, 0)
	assert solve([2, 2], 2) == (0, 1)
