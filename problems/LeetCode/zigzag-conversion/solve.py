def solve(string: str, rows: int) -> str:
	if rows == 1:
		return string

	lines = [list(' ' * len(string)) for _ in range(rows)]
	row = 0
	column = 0
	direction = 'down'
	for char in string:
		lines[row][column] = char
		if direction == 'down':
			row += 1
			if row < len(lines):
				continue
			row -= 2
			column += 2
			direction = 'up'
		else:
			row -= 1
			column += 2
			if row >= 0:
				continue
			row = 1
			column -= 2
			direction = 'down'
	return '\n'.join(''.join(line).strip() for line in lines)


def test_solve():
	assert solve('PAYPALISHIRING', 3) == 'P   A   H   N\nA P L S I I G\nY   I   R'
	assert solve('PAYPALISHIRING', 4) == 'P     I     N\nA   L S   I G\nY A   H R\nP     I'
	assert solve('A', 1) == 'A'
	assert solve('AB', 1) == 'AB'
