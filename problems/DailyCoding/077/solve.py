from typing import List, Tuple



def solve(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
	intervals.sort(key=lambda interval: interval[0])

	i = -1
	while i < len(intervals) - 2:
		i += 1
		first = intervals[i]

		j = i
		while j < len(intervals) - 1:
			j += 1
			considering = intervals[j]
			if first[1] < considering[0]:
				break

			intervals[i] = (first[0], max([first[1], considering[1]]))
			first = intervals[i]
			del intervals[j]
			j -= 1

	return intervals


def test_solve():
	assert solve([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]
	assert solve([(1, 5), (5, 10), (8, 15), (15, 20)]) == [(1, 20)]
	assert solve([(1, 4), (5, 10), (8, 14), (15, 20)]) == [(1, 4), (5, 14), (15, 20)]
