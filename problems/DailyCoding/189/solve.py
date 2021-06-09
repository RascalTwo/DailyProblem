from typing import List, Set



def solve(numbers: List[int]) -> int:
	best = 0
	i = 0
	while i < len(numbers) - best:
		unique: Set[int] = set()
		for j in range(i, len(numbers)):
			num = numbers[j]
			if num in unique:
				break
			unique.add(num)
		best = max(best, len(unique))
		i += 1
	return best



def test_solve():
	assert solve([5, 1, 3, 5, 2, 3, 4, 1]) == 5
	assert solve([1, 2, 3, 4, 5]) == 5
	assert solve([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 2
	assert solve([9, 6, 8, 1, 4, 1, 3, 2, 1, 7, 5]) == 5
