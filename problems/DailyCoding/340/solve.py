import math

from typing import List, Optional, Tuple



def solve(points: List[Tuple[int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
	closest: Tuple[Optional[float], Tuple[Tuple[int, int], Tuple[int, int]]] = (None, tuple())
	for a in points:
		for b in points:
			if a == b:
				continue
			distance = abs(math.sqrt(((b[0] + a[0]) ** 2) + ((b[1] + a[1]) ** 2)))
			if closest[0] is None or distance < closest[0]:
				closest = (distance, (a, b))
	return closest[1]


def test_solve():
	assert solve([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]) == ((1, 1), (-1, -1))
