def solve(string: str) -> str:
	chars = list(string)
	i = 0
	while i != len(chars) - 1:
		j = i + 1
		if chars[i] == chars[j]:
			chars.pop(i)
			chars.pop(i)
			i -= 1
		else:
			i += 1
	return ''.join(chars)


def test_solve():
	assert solve('abbc') == 'ac'
	assert solve('abccbc') == 'ac'
	assert solve('abbbbc') == 'ac'
	assert solve('abbbc') == 'abc'