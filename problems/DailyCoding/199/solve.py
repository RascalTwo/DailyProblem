def solve(string: str) -> str:
	chars = list(string)
	opened = 0
	i = 0
	while i != len(chars):
		char = chars[i]
		if char == '(':
			opened += 1
			i += 1
			continue

		if opened == 0:
			chars.insert(i, '(')
			i += 2
		else:
			opened -= 1
			i += 1

	return ''.join(chars + [')' * opened])


def test_solve():
	assert solve('(()') == '(())'
	assert solve('))()(') == '()()()()'
