def is_sparse(number: int) -> bool:
	return '11' not in bin(number)[2:]


def solve(n: int) -> int:
	if is_sparse(n):
		return n

	while True:
		n += 1
		if is_sparse(n):
			return n


def test_solve():
	assert solve(21) == 21
	assert solve(22) == 32
