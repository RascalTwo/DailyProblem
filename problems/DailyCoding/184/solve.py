def get_gcd(a: int, b: int) -> int:
	return a if not b else get_gcd(b, a % b)


def solve(*numbers: int) -> int:
	gcd = get_gcd(*numbers[:2])
	for number in numbers[2:]:
		gcd = get_gcd(gcd, number)
	return gcd


def test_solve():
	assert solve(42, 56, 14) == 14
