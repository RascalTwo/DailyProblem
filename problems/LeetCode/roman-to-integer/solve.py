from typing import Dict


ROMAN_NUMERALS = {
	'M': 1000,
	'CM': 900,
	'D': 500,
	'CD': 400,
	'C': 100,
	'XC': 90,
	'L': 50,
	'XL': 40,
	'X': 10,
	'IX': 9,
	'V': 5,
	'IV': 4,
	'I': 1
}

def numerals_to_int(numerals: str, encoded: Dict[str, int] = ROMAN_NUMERALS) -> int:
	result = 0
	adding = True
	numerals = numerals[::-1]

	last = None
	for char in numerals:
		value = encoded[char]
		adding = not last or (last and value >= last)
		last = value

		if adding:
			result += value
		else:
			result -= value

	return result


def test_numerals_to_int():
	assert numerals_to_int('MDCLXVI') == 1666
	assert numerals_to_int('XIV') == 14
	assert numerals_to_int('XIII') == 13
	assert numerals_to_int('XX') == 20
	assert numerals_to_int('IX') == 9
	assert numerals_to_int('XL') == 40
	assert numerals_to_int('XXXIX') == 39
	assert numerals_to_int('VIII') == 8
	assert numerals_to_int('II') == 2
	assert numerals_to_int('IV') == 4