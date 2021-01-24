def is_palindrome(string: str) -> bool:
	return string[::-1] == string


def solve(string: str) -> str:
	longest = string[0]

	for i in range(len(string)):
		for j in range(len(string), i, -1):
			substring = string[i:j]
			if is_palindrome(substring) and len(substring) > len(longest):
				longest = substring

	return longest


def test_solve():
	assert solve('aabcdcb') == 'bcdcb'
	assert solve('bananas') == 'anana'
