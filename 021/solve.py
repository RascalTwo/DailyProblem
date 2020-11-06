from typing import List, Tuple



def solve(intervals: List[Tuple[int, int]]):
	times = {}
	for start, end in intervals:
		for time in range(start, end + 1):
			times[time] = times.get(time, 0) + 1

	return max(times.values())


def test_solve():
	assert solve([(30, 75), (0, 50), (60, 150)]) == 2
