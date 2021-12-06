from typing import Tuple



def solve(position: Tuple[int, int], *coins: Tuple[int, int]):
	return min(coins, key = lambda coin: abs(position[0] - coin[0]) + abs(position[1] - coin[1]))


def test_solve():
	assert solve((0, 2), (0, 4), (1, 0), (2, 0), (3, 2)) == (0, 4)
