import collections

from typing import List, Tuple



def solve(letters: str, *edges: Tuple[int, int]):
	best = None

	paths: List[List[int]] = [[origin] for origin, _ in edges]
	while paths:
		path = paths.pop()
		current = path[-1]

		counts = collections.Counter(letters[i] for i in path)
		most_frequent_index = max(counts.keys(), key = lambda key: counts[key])
		current_best = counts[most_frequent_index]
		if best is None:
			best = current_best
		else:
			if counts[most_frequent_index] > best:
				best = current_best

		for origin, dest in edges:
			if origin != current:
				continue
			if dest in path:
				return None
			paths.append([*path, dest])
	return best


def test_solve():
	assert solve('ABACA', (0, 1), (0, 2), (2, 3), (3, 4)) == 3
	assert solve('A', (0, 0)) == None
	assert solve('AZ', (0, 1), (1, 0)) == None
