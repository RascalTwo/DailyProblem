def solve(*strings: str) -> str:
	if not strings:
		return ''

	first = strings[0]
	shortest = min(map(len, strings))

	i = 0
	while i < shortest and all(string[i] == first[i] for string in strings):
		i += 1
	return first[:i]


def test_solve():
	assert solve("flower", "flow", "flight") == "fl"
	assert solve("dog", "racecar", "car") == ""
