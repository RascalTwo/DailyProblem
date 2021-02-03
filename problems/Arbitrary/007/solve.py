def solve(string: str) -> str:
	return ''.join(char.lower() if char.isupper() else char.upper() for char in string)


def test_solve():
	assert solve('hello world') == 'HELLO WORLD'
	assert solve('AbCdEf') == 'aBcDeF'
