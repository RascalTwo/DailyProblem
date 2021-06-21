def cell_address_to_int(address: str) -> int:
	result = 0
	for char in address:
		result = result * 26 + (ord(char) - ord('A')) + 1
	return result


def test_cell_address_to_int():
	assert cell_address_to_int('A') == 1
	assert cell_address_to_int('F') == 6
	assert cell_address_to_int('Z') == 26
	assert cell_address_to_int('AA') == 27
	assert cell_address_to_int('AB') == 28
	assert cell_address_to_int('AD') == 30
	assert cell_address_to_int('AZ') == 52
	assert cell_address_to_int('BA') == 53
	assert cell_address_to_int('BZ') == 78
	assert cell_address_to_int('CA') == 79
	assert cell_address_to_int('YZ') == 676
	assert cell_address_to_int('ZA') == 677
	assert cell_address_to_int('ZZ') == 702
	assert cell_address_to_int('AAA') == 703
	assert cell_address_to_int('AAB') == 704
	assert cell_address_to_int('ALL') == 1000


def int_to_cell_address(number: int) -> str:
	address = ''
	while number:
		number, remaining = divmod(number - 1, 26)
		address = chr(ord('A') + remaining) + address
	return address


def test_int_to_cell_address():
	assert int_to_cell_address(1) == 'A'
	assert int_to_cell_address(6) == 'F'
	assert int_to_cell_address(26) == 'Z'
	assert int_to_cell_address(27) == 'AA'
	assert int_to_cell_address(28) == 'AB'
	assert int_to_cell_address(30) == 'AD'
	assert int_to_cell_address(52) == 'AZ'
	assert int_to_cell_address(53) == 'BA'
	assert int_to_cell_address(61) == 'BI'
	assert int_to_cell_address(78) == 'BZ'
	assert int_to_cell_address(79) == 'CA'
	assert int_to_cell_address(676) == 'YZ'
	assert int_to_cell_address(677) == 'ZA'
	assert int_to_cell_address(702) == 'ZZ'
	assert int_to_cell_address(703) == 'AAA'
	assert int_to_cell_address(704) == 'AAB'
	assert int_to_cell_address(1000) == 'ALL'
