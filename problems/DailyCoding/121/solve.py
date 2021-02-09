def is_palindrome(string: str) -> bool:
	return string[::-1] == string


def solve(string: str, k: int) -> bool:
	if k == 0:
		return is_palindrome(string)

	for i in range(len(string)):
		if solve(string[:i] + string[i+1:], k - 1):
			return True
	return False


def test_solve():
	assert solve('waterrfetawx', 2) is True
	assert solve('ecar', 3) is True
	assert solve('acecar', 1) is True
