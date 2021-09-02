from typing import Iterable



def solve_iter(n: int) -> Iterable[int]:
	while True:
		a = ''.join(sorted(list(str(n))))
		b = a[::-1]
		if b > a:
			a, b = b, a

		n = int(a) - int(b)
		if n == 6174:
			break
		yield n


def solve_recur(n: int) -> Iterable[int]:
	a = ''.join(sorted(list(str(n))))
	b = a[::-1]
	if b > a:
		a, b = b, a

	n = int(a) - int(b)
	if n == 6174:
		return []
	yield n
	yield from solve_recur(n)


def test_solve():
	for solve in (solve_iter, solve_recur):
		assert list(solve(1234)) == [3087, 8352]
