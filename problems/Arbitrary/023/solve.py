def solve(encoded: str) -> str:
	digits = ''
	multiple = 0
	group = ''
	result = ''
	for char in encoded:
		if multiple:
			if char == ']':
				result += group * multiple
				group = ''
				multiple = 0
			else:
				group += char
		else:
			if char.isdigit():
				digits += char
			elif char == '[':
				multiple = int(digits)
				digits = ''
			else:
				result += char

	return result


def test_solve():
	assert solve('3[a]2[bc]') == 'aaabcbc'
	assert solve('2[abc]3[cd]ef') == 'abcabccdcdcdef'
	assert solve('11[ab]rft3[brf]') == 'abababababababababababrftbrfbrfbrf'
