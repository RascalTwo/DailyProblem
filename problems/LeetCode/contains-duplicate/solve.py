from typing import Set



def solve_set(*nums: int):
	return len(set(nums)) != len(nums)


def solve_efficient(*nums: int):
	seen: Set[int] = set()
	for num in nums:
		if num in seen:
			return True
		seen.add(num)
	return False


def test_solve():
	for solve in (solve_set, solve_efficient):
		assert solve(1, 2, 3, 1) == True
		assert solve(1, 2, 3, 4) == False
		assert solve(1, 1, 1, 3, 3, 4, 3, 2, 4, 2) == True
