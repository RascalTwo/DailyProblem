from typing import List, Set, Tuple



def solve(types: List[int], variance: int = 2) -> Tuple[Set[int], int]:
	start = 0
	longest = 0
	for i in range(len(types)):
		for j in range(i, len(types)):
			if len(set(types[i:j])) == variance and (diff := j - i) > longest:
				start, longest = i, diff

	return set(types[start:start + variance + 1]), start


def test_solve():
	assert solve([2, 1, 2, 3, 3, 1, 3, 5]) == ({1, 3}, 3)
