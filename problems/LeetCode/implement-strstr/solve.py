def solve(haystack: str, needle: str) -> int:
	if needle == haystack or not needle:
		return 0
	if not haystack:
		return -1

	for s in range(len(haystack) - len(needle) + 1):
		if haystack[s:s + len(needle)] == needle:
			return s

	return -1


def test_solve():
	assert solve('hello', 'll') == 2
	assert solve('aaaaa', 'bba') == -1
	assert solve('', '') == 0
	assert solve('', 'a') == -1
	assert solve('a', 'a') == 0
	assert solve('abc', 'c') == 2
