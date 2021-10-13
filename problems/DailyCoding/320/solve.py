from typing import Tuple



def solve(string: str) -> Tuple[int, int]:
	unique_chars = set(string)

	best = (0, len(string) - 1)
	for i in range(len(string) - len(unique_chars) + 1):
		for j in range(i + len(unique_chars) - 1, len(string) + 1):
			if set(string[i:j]) == unique_chars and j-1-i < best[1] - best[0]:
				best = i, j-1
	return best


def test_solve():
	assert solve('jiujitsu') in [(2, 6), (3, 7)]
	assert solve('racecar') in [(0, 3), (3, 6)]
