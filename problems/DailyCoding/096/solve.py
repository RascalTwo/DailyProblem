import itertools
from typing import List

def solve(digits: List[int]) -> List[List[int]]:
	return list(map(list, itertools.permutations(digits)))


def test_solve():
	assert solve([1, 2, 3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
