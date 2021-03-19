import math


from typing import List, Tuple



Point = Tuple[int, int]


def distance(a: Point, b: Point) -> float:
	return abs(math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)))


def solve(points: List[Point], center: Point, k: int):
	for i in range(k + 1):
		for j in range(0, len(points) - i - 1):
			if distance(center, points[j]) > distance(center, points[j + 1]):
				points[j], points[j + 1] = points[j + 1], points[j]

	return points[:k]


def test_solve():
	assert solve([(0, 0), (5, 4), (3, 1)], (1, 2), 1) == [(0, 0)]
	assert solve([(0, 0), (5, 4), (3, 1)], (1, 2), 2) == [(0, 0), (3, 1)]
	assert solve([(0, 0), (5, 4), (3, 1)], (1, 2), 3) == [(0, 0), (3, 1), (5, 4)]
