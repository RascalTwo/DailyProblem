from typing import Iterable



def solve(n: int, str: str = '', started: int = 0, finished: int = 0) -> Iterable[str]:
	if finished == n:
		yield str
		return

	if started < n:
		yield from solve(n, str + '(', started + 1, finished)
	if started > finished:
		yield from solve(n, str + ')', started, finished + 1)


def test_solve():
	assert sorted(solve(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
	assert list(solve(1)) == ["()"]
