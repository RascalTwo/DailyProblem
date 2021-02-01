from typing import List



def solve(integers: List[int]) -> List[float]:
	return sorted(v ** 2 for v in integers)


def test_solve():
	assert solve([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
