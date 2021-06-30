def solve(n: int):
	values = [0, 1]
	for _ in range(n - 1):
		values.append(values.pop(0) + values[-1])
	return values[0]


def test_solve():
	for n, value in enumerate([0, 1, 1, 2, 3, 5, 8, 13, 21, 34], 1):
		print(n, value)
		assert solve(n) == value
