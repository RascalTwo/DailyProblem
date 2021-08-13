def solve(n: int) -> bool:
	first, *rest = bin(n)[2:]
	return first == '1' and set(rest) == {'0'} and len(rest) % 2 == 0


def test_solve():
	trues = {4, 16, 64, 256, 1024, 4096, 16384}
	for num in range(1, 20000):
		assert solve(num) is (num in trues)

