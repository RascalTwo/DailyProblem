import itertools


from typing import List



def solve(integers: List[int]) -> int:
	most = '0'
	for order in itertools.permutations(integers):
		most = max(most, ''.join(map(str, order)))
	return int(most)


def test_solve():
	assert solve([10, 7, 76, 415]) == 77641510
