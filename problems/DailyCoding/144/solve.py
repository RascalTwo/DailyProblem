from typing import List, Optional



def solve(array: List[int], index: int) -> Optional[int]:
	target  = array[index]
	best = (None, None)
	for i, num in enumerate(array):
		dist = abs(i - index)
		if num > target and (best[0] is None or best[0] > dist):
			best = (dist, i)

	return best[1]


def test_solve():
	assert solve([4, 1, 3, 5, 6], 0) == 3
	assert solve([4, 1, 3, 5, 6], 1) == 0
