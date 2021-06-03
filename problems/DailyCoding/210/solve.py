from typing import List



def solve(n: int) -> List[int]:
	sequence: List[int] = []
	while n != 1:
		sequence.append(n)
		n = n // 2 if n % 2 == 0 else 3 * n + 1
	return sequence + [1]


def test_solve():
	assert solve(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
