def solve(column_num: int) -> str:
	column_str = ''

	while column_num >= 26:
		column_str += 'A'
		column_num -= 26
	if column_num:
		column_str += chr(64 + divmod(column_num, 26)[1])

	return column_str


def test_solve():
	assert solve(1) == 'A'
	assert solve(6) == 'F'
	assert solve(27) == 'AA'
	assert solve(30) == 'AD'
	assert solve(120) == 'AAAAP'
