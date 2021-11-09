from typing import List, Set, Tuple



def solve(heights: List[int]) -> int:
	points: Set[Tuple[int, int]] = set()
	mx = 0
	my = 0
	for x, height in enumerate(heights):
		mx = max(mx, x)
		for y in range(height):
			points.add((x, y))
			my = max(my, y)

	best = 1
	for sy in range(my + 1):
		for sx in range(mx + 1):
			if (sx, sy) not in points:
				continue

			for ey in range(sy, my + 1):
				for ex in range(sx, mx + 1):
					if (ex, ey) not in points:
						continue

					if (area := ((ey - sy) + 1) * ((ex - sx) + 1)) > best and all((x, y) in points for y in range(sy, ey + 1) for x in range(sx, ex + 1)):
						best = area

	return best


def test_solve():
	assert solve([1, 3, 2, 5]) == 6
	assert solve([1, 1, 1, 1]) == 4
	assert solve([1, 1, 1, 10]) == 10
