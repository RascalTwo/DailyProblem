from typing import List


def solve(nums: List[int], value: int) -> int:
	length = len(nums)

	removing: List[int] = []
	for i, num in enumerate(nums):
		if num == value:
			removing.append(i)

	k = length - len(removing)
	while removing != list(range(k, length)):
		for offset, i in enumerate(range(length - 1, k - 1, -1), 1):
			while removing[-offset] != i:
				current = removing[-offset]
				tmp = nums[current]
				nums[current] = nums[current + 1]
				nums[current + 1] = tmp
				removing[-offset] = current + 1

	return k


def test_solve():
	def assert_solve(nums: List[int], value: int, expected: List[int]):
		assert solve(nums, value) == len(expected)
		assert nums[:len(expected)] == expected
	assert_solve([3, 2, 2, 3], 3, [2, 2])
	assert_solve([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4])
