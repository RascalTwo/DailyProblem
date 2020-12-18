def solve(n: int, x: int) -> int:
	table = []

	for r in range(1, n + 1):
		row = list(range(1, n + 1))
		for c, value in enumerate(row):
			row[c] = r * value
		table.append(row)

	return sum(sum(value == x for value in row) for row in table)


def test_solve():
	assert solve(6, 12) == 4
