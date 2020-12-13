from typing import Tuple



Bishop = Tuple[int, int]


def solve(*bishops: Bishop):
	count = 0

	for i, bishop in enumerate(bishops):
		for other in bishops[i + 1:]:
			count += abs(bishop[0] - other[0]) == abs(bishop[1] - other[1])

	return count


def test_solve():
	assert solve((0, 0), (1, 2), (2, 2), (4, 0)) == 2
