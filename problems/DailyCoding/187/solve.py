from typing import Set, Tuple, TypedDict


Rectangle = TypedDict('Rectangle', { 'top_left': Tuple[int, int], 'dimensions': Tuple[int, int] })

def solve(*rectangles: Rectangle):
	seen: Set[Tuple[int, int]] = set()
	for rectangle in rectangles:
		sx, sy = rectangle['top_left']
		ox, oy = rectangle['dimensions']
		for x in range(sx, sx + ox):
			for y in range(sy, sy + oy):
				coord = (x, y)
				if coord in seen:
					return True
				seen.add(coord)
	return False


def test_solve():
	assert solve({
		"top_left": (1, 4),
		"dimensions": (3, 3)
	},
	{
		"top_left": (-1, 3),
		"dimensions": (2, 1)
	},
	{
		"top_left": (0, 5),
		"dimensions": (4, 3)
	}) is True

	assert solve({
		"top_left": (1, 4),
		"dimensions": (3, 3)
	},
	{
		"top_left": (-1, 3),
		"dimensions": (2, 1)
	}) is False
