import sys

from typing import Dict, List, Tuple


def solve(elevations: Dict[int, int], paths: Dict[Tuple[int, int], int]) -> Tuple[List[int], int]:
	completed: List[List[int]] = []

	possibles: List[Tuple[List[int], bool]] = [([], True)]
	while possibles:
		possible, increasing = possibles.pop()
		current = possible[-1] if possible else 0
		destinations = [path[1] for path in paths.keys() if path[0] == current]

		if possible and current == 0:
			completed.append(possible)
			continue

		curr_elevation = elevations[current]
		for dest in destinations:
			dest_elevation = elevations[dest]
			if not increasing and dest_elevation > curr_elevation:
				continue
			possibles.append((possible + [dest], increasing and dest_elevation >= curr_elevation))

	return min(
		(
			(
				[0] + path,
				paths[(0, path[0])] + sum(paths[(point, path[i + 1])] for i, point in enumerate(path[:-1]))
			)
			for path in completed
		),
		key = lambda pair: pair[1]
	)

def test_solve():
	assert solve({0: 5, 1: 25, 2: 15, 3: 20, 4: 10}, {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
	}) == ([0, 2, 4, 0], 28)
