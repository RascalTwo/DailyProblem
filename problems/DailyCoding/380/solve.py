from typing import Tuple



def solve(product: int, divisor: int) -> Tuple[int, int]:
	dividend = 0
	while product > divisor:
		dividend += 1
		product -= divisor

	return dividend, product


def test_solve():
	assert solve(10, 3) == (3, 1)
