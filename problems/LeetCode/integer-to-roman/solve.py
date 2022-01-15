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


def int_to_numerals(number: int, encoded: Dict[str, int] = ROMAN_NUMERALS) -> str:
	numerals: str = ''

	for symbol, value in encoded.items():
		multiple, number = divmod(number, value)
		numerals += symbol * multiple

	return numerals


def test_int_to_numerals():
	assert int_to_numerals(1666) == 'MDCLXVI'
	assert int_to_numerals(14) == 'XIV'
	assert int_to_numerals(13) == 'XIII'
	assert int_to_numerals(20) == 'XX'
	assert int_to_numerals(9) == 'IX'
	assert int_to_numerals(40) == 'XL'
	assert int_to_numerals(39) == 'XXXIX'
	assert int_to_numerals(8) == 'VIII'
	assert int_to_numerals(2) == 'II'
	assert int_to_numerals(4) == 'IV'
