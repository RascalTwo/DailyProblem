def solve(string: str) -> str:
	chars = list(string)

	for i in range(len(chars)):
		if not i or chars[i - 1].isspace():
			chars[i] = chars[i].upper()

	return ''.join(chars)


def test_solve():
	assert solve('hello world') == 'Hello World'
	assert solve('How are you doing, this...  lovely day?') == 'How Are You Doing, This...  Lovely Day?'
