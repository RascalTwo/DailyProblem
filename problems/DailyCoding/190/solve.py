from typing import List



def solve(numbers: List[int]) -> int:
	best = 0

	paths = [[i] for i in range(len(numbers))]
	while paths:
		path = paths.pop()
		if len(path) == len(numbers) - 1:
			continue

		last_index = path[-1]
		next_index = (last_index + 1) % len(numbers)
		next_path = path + [next_index]
		best = max(best, sum(numbers[i] for i in next_path))
		paths.append(next_path)

	return best


def test_solve():
	assert solve([8, -1, 3, 4]) == 15
	assert solve([-4, 5, 1, 0]) == 6
