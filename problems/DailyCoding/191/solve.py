from typing import Dict, List, Tuple



def solve(intervals: List[Tuple[int, int]]) -> int:
	original_length = len(intervals)
	while True:
		interval_values: Dict[int, Tuple[List[int], int]] = {
			i: (list(range(start, end + 1)), 0)
			for i, (start, end) in enumerate(intervals)
		}
		for i, (values, _) in interval_values.items():
			inner = values[1:-1]
			overlap_count = 0
			for j, (other_values, _) in interval_values.items():
				if i == j:
					continue
				if any(value in other_values for value in inner):
					overlap_count += 1
			interval_values[i] = (values, overlap_count)

		most_overlapping = next(iter(sorted(interval_values.items(), key = lambda pair: pair[1][1], reverse=True)))
		if not most_overlapping[1][1]:
			break
		intervals.pop(most_overlapping[0])
	return original_length - len(intervals)


def test_solve():
	assert solve([(0, 1), (1, 2)]) == 0
	assert solve([(7, 9), (2, 4), (5, 8)]) == 1
	assert solve([(0, 10), (2, 4), (4, 6)]) == 1
	assert solve([(0, 10), (2, 4), (4, 6), (6, 8), (-5, 10)]) == 2
