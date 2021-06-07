from typing import Dict



def solve(numerals: str, encoded: Dict[str, int] = {
	'M': 1000,
	'D': 500,
	'C': 100,
	'L': 50,
	'X': 10,
	'V': 5,
	'I': 1
}) -> int:
	result = 0
	adding = True
	numerals = numerals[::-1]

	last = None
	for char in numerals:
		value = encoded[char]
		adding = not last or (last and value > last)
		last = value

		if adding:
			result += value
		else:
			result -= value

	return result


def test_solve():
	assert solve('MDCLXVI') == 1666
	assert solve('XIV') == 14
	assert solve('XIIV') == 13
	assert solve('IX') == 9
	assert solve('XL') == 40
	assert solve('XXXIL') == 39
	assert solve('IIIV') == 2
	assert solve('IV') == 4
