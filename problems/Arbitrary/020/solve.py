
import collections


from typing import Counter, List



def solve(integers: List[int]) -> List[int]:
	counts: Counter[int] = collections.Counter(integers)
	return sorted(counts.keys(), key = lambda num: (-counts[num], num))


def test_solve():
	assert solve([]) == []
	assert solve([2]) == [2]
	assert solve([2, 2, 2, 2]) == [2]
	assert solve([3, 3, 2, 2]) == [2, 3]
	assert solve([3, 3, 2, 2, 3]) == [3, 2]
	assert solve([-1, -3, 0, -3, 5, 5, 5]) == [5, -3, -1, 0]
