def last_valid_index(string: str, exponent: bool) -> int:
	sign = False
	digits = False
	dot = not exponent
	i = -1
	for i, char in enumerate(string):
		if char.isdigit():
			digits = True
			continue
		elif char in '+-':
			if sign or i:
				return -1
			sign = True
			continue
		elif char == '.':
			if dot:
				return -1
			dot = True
			continue
		elif char in 'eE':
			if not i or not exponent or not digits:
				return -1
			result = last_valid_index(string[i + 1:], False)
			if result == -1:
				return -1
			return i + 1 + result
		return i - 1
	return i if digits else -1


def solve(string: str) -> bool:
	return last_valid_index(string, True) == len(string) - 1


def test_solve():
	assert solve('2') is True
	assert solve('0089') is True
	assert solve('-0.1') is True
	assert solve('+3.14') is True
	assert solve('4.') is True
	assert solve('-.9') is True
	assert solve('2e10') is True
	assert solve('-90E3') is True
	assert solve('3e+7') is True
	assert solve('+6e-1') is True
	assert solve('53.5e93') is True
	assert solve('-123.456e789') is True
	assert solve('abc') is False
	assert solve('1a') is False
	assert solve('1e') is False
	assert solve('e3') is False
	assert solve('99e2.5') is False
	assert solve('--6') is False
	assert solve('-+3') is False
	assert solve('95a54e53') is False
	assert solve('6+1') is False
	assert solve('.-4') is False
	assert solve('.e1') is False


