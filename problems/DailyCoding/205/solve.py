import sys
import itertools


def solve(integer: int):
	best = (integer, sys.maxsize)
	for permutation in itertools.permutations(str(integer)):
		number = int(''.join(permutation))
		diff = number - integer
		if diff > 0 and diff < best[1]:
			best = number, diff
	return best[0]


def test_solve():
	assert solve(123) == 132
	assert solve(978) == 987
	assert solve(654) == 654