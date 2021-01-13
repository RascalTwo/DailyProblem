from typing import List, Optional



def solve(integers: List[int], i: int = 0, origin: Optional[int] = None) -> bool:
	if i == len(integers) - 1:
		return True

	if i >= len(integers) or i < 0:
		return False

	return False if not (hop := integers[i]) else (
		(solve(integers, i - hop, i) if i - hop != origin else False)
		or
		(solve(integers, i + hop, i) if i + hop != origin else False)
	)


def test_solve():
	assert solve([2, 0, 1, 0]) is True
	assert solve([1, 1, 0, 1]) is False
	assert solve([2, 3, 1, 0, 0]) is True
