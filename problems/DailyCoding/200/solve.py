import collections
import sys


from typing import DefaultDict, List, Tuple



def solve(*points: Tuple[int, int]) -> List[int]:
	counts: DefaultDict[int, List[int]] = collections.defaultdict(list)
	least = sys.maxsize
	most = -sys.maxsize
	for start, end in points:
		least = min(least, start)
		most = max(most, end)
		counts[start].append(end)
		counts[end].append(start)
	del counts[least]
	del counts[most]

	results: List[int] = []
	remaining = list(counts.items())
	while remaining:
		remaining = sorted(remaining, key=lambda pair: len(pair[1]))
		removing_key, removing_values = remaining.pop()
		results.append(removing_key)

		for k, vs in remaining:
			if removing_key in vs:
				vs.remove(removing_key)
			if k in removing_values and not vs:
				remaining.remove((k, vs))

	return list(reversed(results))


def test_solve():
	assert solve((1, 4), (4, 5), (7, 9), (9, 12)) == [4, 9]
	assert solve((1, 2), (2, 3), (3, 4), (4, 5), (5, 6)) == [2, 3, 5]
