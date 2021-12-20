import itertools
import collections

from typing import Counter, List, Tuple



def are_overlap_free(*jobs: Tuple[int, int]) -> bool:
	times: Counter[int] = collections.Counter()
	for start, end in jobs:
		for time in range(start, end):
			times[time] += 1
			if times[time] > 1:
				return False
	return True


def solve(*jobs: Tuple[int, int]) -> List[Tuple[int, int]]:
	return list(max((combo for count in range(len(jobs) - 1, -1, -1) for combo in itertools.combinations(jobs, r=count) if are_overlap_free(*combo)), key = len))


def test_solve():
	assert solve((0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)) == [(1, 4), (4, 7), (8, 11)]
