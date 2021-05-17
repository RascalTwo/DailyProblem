from typing import List, Tuple

Point = Tuple[int, int]
ABC = Tuple[int, int, int]



def points_to_abc(origin: Point, dest: Point) -> ABC:
	a = dest[1] - origin[1]
	b = origin[0] - dest[0]
	return a, b, (a * origin[0]) + (b * origin[1])


def does_line_intersect(a: ABC, b: ABC) -> bool:
	return not (a[0] * b[1]) - (a[1] * b[0])



def solve(a: List[Point], b: List[Point]) -> int:
	points: List[ABC] = []
	for i in range(len(a)):
		points.append(points_to_abc(a[i], b[i]))

	intersections = 0
	for i in range(len(points) - 1):
		for j in range(i + 1, len(points)):
			intersections += does_line_intersect(points[i], points[j])

	return intersections


def test_solve():
	assert solve([(1, 0), (2, 0), (3, 0)], [(1, 1), (2, 1), (3, 1)]) == 3
