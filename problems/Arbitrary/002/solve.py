from typing import List, Optional



def average(integers: List[int]) -> float:
	return sum(integers) / len(integers) if len(integers) else 0


def solve(integers: List[int]) -> Optional[int]:
	best = (None, None)
	for i in range(len(integers)):
		diff = abs(average(integers[0:i]) - average(integers[i + 1:]))
		if best[0] is None or diff < best[0]:
			best = (diff, i)

	return best[1]



def test_solve():
	assert solve([7, 1, 4, 3]) == 2
	assert solve([2, 3, 20, 3, 2]) == 2
	assert solve([3, 4, 3, 2]) == 1
	assert solve([]) is None
