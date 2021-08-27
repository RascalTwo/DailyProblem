import collections

from typing import Counter, List



def solve(row_lengths: List[List[int]]) -> int:
	counts: Counter[int] = collections.Counter()

	for lengths in row_lengths:
		last = 0
		for length in lengths[:-1]:
			last += length
			counts[last] += 1

	return max(counts.keys(), key = lambda key: counts[key])


def test_solve():
	assert solve([
		[3, 5, 1, 1],
		[2, 3, 3, 2],
		[5, 5],
		[4, 4, 2],
		[1, 3, 3, 3],
		[1, 1, 6, 1, 1]
	]) == 8
