from typing import List



def solve(lst: List[int], i: int, j: int):
	return lst[0:i] + lst[::-1][i:j+1] + lst[j+1:len(lst)]


def test_solve():
	assert solve([1, 2, 3, 4], 0, 3) == [4, 3, 2, 1]
	assert solve([1, 2, 3, 4, 5, 6], 1, 4) == [1, 5, 4, 3, 2, 6]
