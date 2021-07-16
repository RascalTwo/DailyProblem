import collections

from typing import DefaultDict, List


def solve(citations: List[int])  -> int:
	h_indexes: DefaultDict[int, int] = collections.defaultdict(int)
	for count in citations:
		for h in range(count + 1):
			h_indexes[h] += 1

	return next(
		h
		for h, count in
		sorted(
			h_indexes.items(),
			key=lambda pair: pair[0], reverse=True
		)
		if count >= h
	)


def test_solve():
	assert solve([4, 3, 0, 1, 5]) == 3
