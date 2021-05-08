from typing import List, Set, Tuple



def solve(numbers: List[int], s1: Set[int] = set(), s2: Set[int] = set()) -> Tuple[int, Set[int], Set[int]]:
	if not numbers:
		return abs(sum(s1) - sum(s2)), s1, s2

	number, rest = numbers[0], numbers[1:]
	addition = set([number])
	inc = solve(rest, s1 | addition, s2)
	exc = solve(rest, s1, s2 | addition)

	return inc if inc[0] < exc[0] else exc


def test_solve():
	assert solve([5, 10, 15, 20, 25])[0] == 5
