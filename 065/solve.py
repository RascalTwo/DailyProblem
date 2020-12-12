from typing import Iterable, List



CHANGES = [
	0 + 1j,
	1 + 0j,
	0 + -1j,
	-1 + 0j,
]


def solve(matrix: List[List[int]]) -> Iterable[int]:
	seen = set()

	change = 0 + 1j
	loc = 0 + 0j
	while loc not in seen:
		yield matrix[int(loc.real)][int(loc.imag)]
		seen.add(loc)

		forward = loc + change
		if forward in seen or forward.real < 0 or forward.real >= len(matrix) or forward.imag < 0 or forward.imag >= len(matrix[int(forward.real)]):
			change = CHANGES[(CHANGES.index(change) + 1) % 4]
			forward = loc + change

		loc = forward


def test_solve():
	assert list(solve([
		[1,  2,  3,  4,  5],
		[6,  7,  8,  9,  10],
		[11, 12, 13, 14, 15],
		[16, 17, 18, 19, 20]
	])) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
	assert list(solve([
		[1, 2],
		[4, 3]
	])) == [1, 2, 3, 4]
	assert list(solve([
		[1, 2, 3],
		[8, 9, 4],
		[7, 6, 5]
	])) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
