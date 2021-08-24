# Count all possible btrees with N nodes

from typing import Dict


def solve_memo(n: int) -> int:
	memo: Dict[int, int] = {}

	def recur(n: int) -> int:
		if n in memo:
			return memo[n]

		if n <= 1:
			return 1

		res = 0
		for i in range(1, n + 1):
			res += (
				recur(i - 1) *
				recur(n - i)
			)

		memo[n] = res
		return res

	return recur(n)


def solve_recur(n: int) -> int:
	return 1 if n <= 1 else sum(solve_recur(i - 1) * solve_recur(n - i) for i in range(1, n + 1))


def test_solve():
	for solve in (solve_memo, solve_recur):
		assert solve(1) == 1
		assert solve(2) == 2
		assert solve(3) == 5
		assert solve(4) == 14
		assert solve(5) == 42
		assert solve(6) == 132
		assert solve(7) == 429
		assert solve(8) == 1430
		assert solve(9) == 4862
		assert solve(10) == 16796
		assert solve(15) == 9694845