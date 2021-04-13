from typing import Iterable, List, Set



def solve_iter(step_count: int, steps_per_step: Set[int] = {1, 2}) -> List[List[int]]:
	complete: List[List[int]] = []
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


def solve_recur(step_count: int, steps_per_step: Set[int] = {1, 2}, steps_taken: List[int] = []) -> Iterable[List[int]]:
	current_step = sum(steps_taken)
	if current_step >= step_count:
		if current_step == step_count:
			yield steps_taken
		return

	for step in steps_per_step:
		yield from solve_recur(step_count, steps_per_step, steps_taken + [step])


def test_solve():
	for solve in (solve_iter, solve_recur):
		assert sorted(list(solve(4))) == [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
		assert sorted(list(solve(3))) == [[1, 1, 1], [1, 2], [2, 1]]
		assert sorted(list(solve(5))) == [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1], [1, 2, 2], [2, 1, 1, 1], [2, 1, 2], [2, 2, 1]]
