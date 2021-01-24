def decode(encoded: str) -> str:
	result = ''

	multiplier = ''
	for char in encoded:
		if char.isdigit():
			multiplier += char
		else:
			result += int(multiplier) * char
			multiplier = ''

	return result


def encode(string: str) -> str:
	if not string:
		return ''

	result = ''
	duplicates = string[0]
	for i, char in enumerate(string[1:]):
		if char in duplicates:
			duplicates += char
		else:
			result += f'{len(duplicates)}{duplicates[0]}'
			duplicates = string[i + 1]

	result += f'{len(duplicates)}{duplicates[0]}'
	return result


def test_solve():
	assert encode('') == ''
	assert decode('') == ''

	assert encode('A') == '1A'
	assert decode('1A') == 'A'

	assert encode('AAA') == '3A'
	assert decode('3A') == 'AAA'

	assert encode('AAAABBBCCDAA') == '4A3B2C1D2A'
	assert decode('4A3B2C1D2A') == 'AAAABBBCCDAA'

	assert encode('BAAAAAAAAAAAAAAAB') == '1B15A1B'
	assert decode('1B15A1B') == 'BAAAAAAAAAAAAAAAB'
