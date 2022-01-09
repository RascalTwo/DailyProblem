def solve(string: str) -> str:
	if not string:
		return ''

	best = string[0]
	for start in range(len(string)):
		for end in range(start + 1, len(string) + 1):
			substring = string[start:end]
			if len(set(substring)) == (length := len(substring)) and length > len(best):
				best = substring
	return best


def test_solve():
	assert solve('abcabcbb') == 'abc'
	assert solve('bbbbb') == 'b'
	assert solve('pwwkew') == 'wke'
	assert solve('au') == 'au'
	assert solve('') == ''
