from typing import List, Set



def solve(step_count: int, steps_per_step: Set[int] = {1, 2}) -> List[List[int]]:
	complete = []
	building = [[0]]
	while building:
		path = building.pop(0)
		for i in steps_per_step:
			if (next_index := path[-1] + i) <= step_count:
				(building, complete)[next_index == step_count].append(path + [next_index])

	return [
		[path[i + 1] - path[i] for i in range(len(path) - 1)]
		for path in reversed(complete)
	]


def test_solve():
	assert solve(4) == [[1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2]]
