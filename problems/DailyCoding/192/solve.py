from typing import List



def solve_recur(steps: List[int]) -> bool:
	return len(steps) == 1 or any(solve_recur(steps[i:]) for i in range(1, steps[0] + 1))


def solve_backtrack(steps: List[int]) -> bool:
	backtracking = [len(steps) - 1]

	while backtracking:
		i = backtracking.pop()
		for o in range(i - 1, -1, -1):
			if steps[o] + o >= i:
				if o == 0:
					return True
				backtracking.append(o)

	return False


def test_solve():
	for solve in (solve_backtrack, solve_recur):
		assert solve([2, 3, 1, 1, 4]) is True
		assert solve([1, 3, 1, 2, 0, 1]) is True
		assert solve([1, 2, 1, 0, 0]) is False
		assert solve([3, 1, 2, -2, 0]) is True
