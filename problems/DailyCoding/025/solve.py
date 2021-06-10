def solve(regex: str, string: str):
	last = ''
	while regex and string:
		symbol = regex[0]
		if symbol not in '.*':
			if string[0] != symbol:
				return False
			string = string[1:]
		elif symbol == '.':
			string = string[1:]
		elif symbol == '*':
			while string:
				if solve(regex[1:], string):
					return True

				if last == '.':
					string = string[1:]
					continue
				if last != string[0]:
					string = string[1:]
				else:
					break

		last = symbol
		regex = regex[1:]

	return not string and not regex


def test_solve():
	assert solve('ra.', 'ray') is True
	assert solve('ra.', 'raymond') is False
	assert solve('.*at', 'chat') is True
	assert solve('.*at', 'chats') is False
	assert solve('.*', 'hello world') is True
	assert solve('abc.*', 'hello world') is False
	assert solve('hel*o .*rld', 'hello world') is True
