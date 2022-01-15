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
