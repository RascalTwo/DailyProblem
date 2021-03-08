import collections


from typing import List



def solve(integers: List[int]) -> List[int]:
	return [key for key, value in collections.Counter(integers).items() if value == 1]


def test_solve():
	assert solve([2, 4, 6, 8, 10, 2, 6, 10]) == [4, 8]
