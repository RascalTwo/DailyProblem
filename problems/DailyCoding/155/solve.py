import collections
import math


from typing import Counter, List, Optional



def solve(elements: List[int]) -> Optional[int]:
	counts: Counter[int] = collections.Counter()

	for element in elements:
		counts[element] += 1
		if counts[element] >= math.ceil(len(elements) / 2):
			return element
	return None


def test_solve():
	assert solve([1, 2, 1, 1, 3, 4, 1]) == 1
	assert solve([0, 1, 0, 2, 0]) == 0
	assert solve([0, 1, 0, 2, 1]) == None
	assert solve([9, 8, 8, 7]) == 8
