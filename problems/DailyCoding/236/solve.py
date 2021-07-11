import math

from typing import List, Tuple, Union

Number = Union[int, float]
Point = Tuple[Number, Number]
Line = Tuple[Point, Point]



def is_counter_clockwise(a: Point, b: Point, c: Point):
	return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])


def do_segments_intersect(a: Line, b: Line) -> bool:
	return is_counter_clockwise(a[0], b[0], b[1]) != is_counter_clockwise(a[1], b[0], b[1]) and is_counter_clockwise(a[0], a[1], b[0]) != is_counter_clockwise(a[0], a[1], b[1])


def extend_line(a: Point, b: Point, a_dist: float, b_dist: float) -> Line:
	line_length = math.sqrt(math.pow(a[0] - b[0], 2) + math.pow(a[1] - b[1], 2))
	x_comp = (b[0] - a[0]) / line_length
	y_comp = (b[1] - a[1]) / line_length
	return (
		(a[0] - x_comp * a_dist, a[1] - y_comp * a_dist),
		(b[0] + x_comp * b_dist, b[1] + y_comp * b_dist)
	)


def solve(points: List[Point], considering: Point):
	edges: List[Line] = []
	for i, point in enumerate(points[:-1]):
		edges.append((point, points[i+1]))
	edges.append((points[-1], points[0]))

	# min, max, mean
	bounds: Tuple[List[Number], List[Number]] = tuple([points[0][i], points[0][i], points[0][i]] for i in range(2))
	for point in points[1:]:
		for bound in bounds:
			bound[0] = min(bound[0], point[0])
			bound[1] = max(bound[1], point[0])
			bound[2] += point[0]

	for bound in bounds:
		bound[2] /= len(points)

	center = tuple(bound.pop(2) for bound in bounds)
	extended = extend_line(considering, center, 0, 1)
	for i in range(2, 1000):
		xmin, xmax = bounds[0]
		ymin, ymax = bounds[1]
		for x, y in extended:
			xmin = min(xmin, x)
			xmax = max(xmax, x)
			ymin = min(ymin, y)
			ymax = max(ymax, y)
		if xmin < bounds[0][0] and ymin < bounds[1][0]:
			break
		if xmax > bounds[0][1] and ymax > bounds[1][1]:
			break
		extended = extend_line(considering, center, 0, i)

	return sum(do_segments_intersect(edge, extended) for edge in edges) % 2 == 1


def test_solve():
	assert solve([(3, -8), (6, 5), (4, 8), (-3, 4), (-6, -4)], (0, 0)) is True
	assert solve([(3, -8), (6, 5), (4, 8), (-3, 4), (-6, -4)], (3, 6)) is True
	assert solve([(3, -8), (6, 5), (4, 8), (-3, 4), (-6, -4)], (6, 3)) is False
