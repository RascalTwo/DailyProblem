from typing import List, Optional



def solve(integers: List[int]) -> int:
	most: Optional[int] = None

	for i, first in enumerate(integers):
		for j, second in enumerate(integers[i + 1:]):
			for third in integers[j + 1:]:
				total = first * second * third
				if most is None or total > most:
					most = total

	assert most
	return most


def test_solve():
	assert solve([-10, -10, 5, 2]) == 500
