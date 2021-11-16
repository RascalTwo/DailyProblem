flipable = set([1, 6, 8, 9])
replacements = {6: 9, 9: 6}


def solve(number: int):
	digits = [int(digit) for digit in str(number)]
	if set(digits).difference(flipable):
		return False
	digits = [replacements.get(digit, digit) for digit in digits[::-1]]
	return int(''.join(map(str, digits))) == number


def test_solve():
	assert solve(16891) == True
	assert solve(168891) == True
	assert solve(1689) == False
