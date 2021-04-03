def solve_chars(number: int) -> int:
	return int(''.join(str(int(not int(value))) for value in bin(number)[2:]), 2)


def solve_xor(number: int) -> int:
	return int(bin(number ^ (2 ** (len(bin(number)) - 1) - 1))[3:], 2)


def test_solve():
	for solve in (solve_xor, solve_chars):
		assert solve(0b101) == 0b010
		assert solve(0b11110000111100001111000011110000) == 0b00001111000011110000111100001111
