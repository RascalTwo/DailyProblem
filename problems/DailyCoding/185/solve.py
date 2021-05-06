import collections


from typing import DefaultDict, Tuple, TypedDict



Rectangle = TypedDict('Rectangle', { 'top_left': Tuple[int, int], 'dimensions': Tuple[int, int]})

def solve(*rectangles: Rectangle):
	filled: DefaultDict[Tuple[int, int], int] = collections.defaultdict(int)

	for rectangle in rectangles:
		sx, sy = rectangle['top_left']
		ox, oy = rectangle['dimensions']
		for x in range(sx, sx + ox):
			for y in range(sy, sy + oy):
				filled[(x, y)] += 1

	return len([True for value in filled.values() if value == len(rectangles)])


def test_solve():
	assert solve({
    "top_left": (1, 4),
    "dimensions": (3, 3)
	}, {
    "top_left": (0, 5),
    "dimensions": (4, 3)
	}) == 6
