from typing import List



def solve(integers: List[int]) -> int:
	unique = set()
	total = 0
	for n in integers:
		unique.add(n)
		total += n

	return (3 * sum(unique) - total) // 2


def test_solve():
	assert solve([6, 1, 3, 3, 3, 6, 6]) == 1
	assert solve([13, 19, 13, 13]) == 19
