from typing import Dict



def solve(snakes: Dict[int, int], ladders: Dict[int, int]):

	rolls = 0

	current = 1
	while current != 100:
		best_dest = current
		for i in range(min(100 - current, 6), -1, -1):
			dest = current + i
			best_dest = max(best_dest, dest, ladders.get(dest, 0))
		current = best_dest

		rolls += 1
	return rolls


def test_solve():
	assert solve({16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}, {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}) == 7
