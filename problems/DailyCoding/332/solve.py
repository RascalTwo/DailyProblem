from typing import Iterable, Tuple



def solve(m: int, n: int) -> Iterable[Tuple[int ,int]]:
	for a in range(1, m//2):
		b = m - a
		if a ^ b == n:
			yield a, b


def test_solve():
	assert list(solve(23, 23)) == [(1, 22), (2, 21), (3, 20), (4, 19), (5, 18), (6, 17), (7, 16)]
