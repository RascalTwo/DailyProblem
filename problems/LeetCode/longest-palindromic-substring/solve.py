def solve(string: str) -> str:
	if not string:
		return ''
	best = string[0]
	for start in range(len(string) - 1):
		for end in range(len(string), start, -1):
			if end - start > len(best) and (substring := string[start:end]) == substring[::-1]:
				best = substring
	return best


def test_solve():
	assert solve('babad') in ('aba', 'bab')
	assert solve('cbbd') == 'bb'
	assert solve('aacabdkacaa') == 'aca'