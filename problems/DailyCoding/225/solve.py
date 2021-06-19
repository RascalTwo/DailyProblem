def solve(n: int, k: int) -> int:
	k -= 1

	prisoners = list(range(1, n + 1))
	i = k
	while len(prisoners) > 1:
		prisoners.pop(i)
		i = (i + k) % len(prisoners)

	return prisoners[0]


def test_solve():
	assert solve(5, 2) == 3
	assert solve(10, 3) == 4
