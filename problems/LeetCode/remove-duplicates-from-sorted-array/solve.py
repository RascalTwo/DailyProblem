from typing import List



def solve(nums: List[int]) -> int:
	length = len(nums)
	if length <= 1:
		return length

	removing: List[int] = []
	i = 0
	while i != length - 1:
		if nums[i] == nums[i + 1]:
			removing.append(i)
		i += 1

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
	def assert_solve(nums: List[int], expected: List[int]):
		assert solve(nums) == len(expected)
		assert nums[:len(expected)] == expected
	assert_solve([1, 1, 2], [1, 2])
	assert_solve([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
