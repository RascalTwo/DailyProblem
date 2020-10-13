import math

from typing import List



def solve(integers: List[int]) -> List[int]:
	return [
		math.prod(integers[0:i] + integers[i + 1:])
		for i in range(len(integers))
	]


def test_solve():
	assert solve([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
	assert solve([3, 2, 1]) == [2, 3, 6]

