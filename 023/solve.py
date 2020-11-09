import collections
import sys


from typing import Any, Callable, List, Optional, Tuple, TypeVar



T = TypeVar('T')

Matrix = List[List[T]]
Point = Tuple[int, int]


in_matrix: Callable[[Point, Matrix[Any]], bool] = lambda coord, matrix: 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[coord[0]])


def solve(matrix: Matrix[bool], start: Point, end: Point) -> Optional[int]:
	unvisited = set((r, c) for r in range(len(matrix)) for c in range(len(matrix[r])))
	walls = set((r, c) for (r, c) in unvisited if matrix[r][c] is True)
	unvisited -= walls

	distances = collections.defaultdict(lambda: sys.maxsize, { start: 0 })
	current = start
	while True:
		row, col = current
		distance = distances[current] + 1

		distances.update({
			neighbor: distance
			for neighbor in [
				(row + ro, col + co)
				for ro, co in ((-1, 0), (1, 0), (0, -1), (0, 1))
			]
			if in_matrix(neighbor, matrix) and neighbor not in walls and (neighbor not in distances or distances[neighbor] > distance)
		})

		next_node_distance: Tuple[Optional[Point], int] = (None, sys.maxsize)
		for node in unvisited:
			if node in distances and (distances[node] < next_node_distance[1] or node == end):
				next_node_distance = (node, distances[node])

		next_node = next_node_distance[0]
		if not next_node:
			return None

		current = next_node
		unvisited.remove(current)
		if next_node == end:
			break

	return distances[current]


def test_solve():
	assert solve([
		[False, False, False, False],
		[True,  True,  False, True ],
		[False, False, False, False],
		[False, False, False, False]
	], (3, 0), (0, 0)) == 7
	assert solve([
		[False, False, False, False],
		[False, True , True , True],
		[False, False, False, False],
		[True , True , True , False],
		[False, False, False, False]
	], (4, 0), (0, 3)) == 13
	assert solve([
		[False, False, False, False],
		[True,  True,  True , True ],
		[False, False, False, False],
		[False, False, False, False]
	], (3, 0), (0, 0)) == None

	for corner in ((0, 0), (4, 4), (4, 0), (0, 4)):
		assert solve([
			[False, True , False, False, False],
			[False, False, False, False, True ],
			[False, False, False, False, False],
			[True , False, False, False, False],
			[False, False, False, True , False]
		], (2, 2), corner) == 4
