def solve(needle: str, haystack: str) -> bool:
	if not needle:
		return True

	length = len(needle)
	i = 0
	for char in haystack:
		if needle[i] == char:
			i += 1
		if i >= length:
			return True

	return i == length


def test_solve():
	assert solve("", "ahbgdc") == True
	assert solve("a", "") == False
	assert solve("", "") == True
	assert solve("abc", "ahbgdc") == True
	assert solve("axc", "ahbgdc") == False