from typing import List



def solve(integers: List[int]) -> int:
	last_index = len(integers) - 1

	paths = [[0], [1]]
	best = ([], 0)
	while paths:
		path = paths.pop(0)
		for i in (2, 3):
			if (next_index := path[-1] + i) <= last_index:
				paths.append(path + [next_index])

		if (total := sum(integers[i] for i in path)) > best[1]:
			best = (path, total)

	return best[1]


def test_solve():
	assert solve([2, 4, 6, 2, 5]) == 13
	assert solve([5, 1, 1, 5]) == 10
	assert solve([10, 0, 0, 0, 10, 0, 10, 0, 5, 10, 10]) == 45
