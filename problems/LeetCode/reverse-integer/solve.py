def solve(integer: int) -> int:
	sign = -1 if integer < 0 else 1
	integer *= sign

	value = 0
	while integer:
		integer, digit = divmod(integer, 10)

		value = (value * 10) + digit
		if not (-2147483648 <= value <= 2147483647):
			return 0

	return value * sign


def test_solve():
	assert solve(123) == 321
	assert solve(-123) == -321
	assert solve(120) == 21
	assert solve(2147483647) == 0
