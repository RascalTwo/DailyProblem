from typing import Dict, List, Tuple



def is_within(value: int, a: int, b: int) -> bool:
	if a > b:
		a, b = b, a
	return value in range(a, b + 1)


def solve(relations: List[str]) -> bool:
	rules: List[Tuple[str, Tuple[int, int], str]] = []
	for relation in relations:
		dest, change, origin = relation.split(' ')
		offset = {
			'N': (-1, 0),
			'NE': (-1, 1),
			'E': (0, 1),
			'SE': (1, 1),
			'S': (1, 0),
			'SW': (1, -1),
			'W': (0, -1),
			'NW': (-1, -1)
		}[change]
		rules.append((dest, offset, origin))

	positions: Dict[str, Tuple[int, int]] = {}
	for dest, offset, origin in rules:
		origin_loc = positions.get(origin, None)
		dest_loc = positions.get(dest, None)
		if dest_loc and not origin_loc:
			origin, dest = dest, origin
			origin_loc, dest_loc = dest_loc, origin_loc
			offset = (-offset[0], -offset[1])

		if not origin_loc and not dest_loc:
			origin_loc = (0, 0)
			positions[origin] = origin_loc

		assert origin_loc
		if not dest_loc:
			dest_loc = origin_loc
		dest_loc = (dest_loc[0] + offset[0], dest_loc[1] + offset[1])
		positions[dest] = dest_loc

	for dest, offset, origin in rules:
		for _ in range(2):
			dest_loc = positions[dest]
			origin_loc = positions[origin]
			if not is_within(origin_loc[0] + offset[0], origin_loc[0], dest_loc[0]):
				return False
			if not is_within(origin_loc[1] + offset[1], origin_loc[1], dest_loc[1]):
				return False
			dest, origin = origin, dest
			offset = (-offset[0], -offset[1])

	return True


def test_solve():
	assert solve(['A NE B']) is True
	assert solve(['N N C', 'NE NE C', 'E E C', 'SE SE C', 'S S C', 'SW SW C', 'W W C', 'NW NW C']) is True
	assert solve(['N N C', 'NE NE C', 'E E C', 'SE SE C', 'S S C', 'SW SW C', 'W W C', 'NW NW C', 'S N N']) is False
	assert solve(['A N B', 'C N A']) is True
	assert solve(['C N A', 'A N B']) is True
	assert solve(['A SW C']) is True
	assert solve(['A N B', 'B NE C', 'C N A']) is False
	assert solve(['A NW B', 'A N B']) is True
