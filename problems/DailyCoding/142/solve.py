def solve(string: str, opened: int = 0) -> bool:
	opened = 0

	for i, char in enumerate(string):
		if char == '*':
			if any(solve(sub + string[i + 1:], opened) for sub in ' ()'):
				return True
		elif char == '(':
			opened += 1
		elif char == ')':
			if not opened:
				return False
			opened -= 1

	return not opened


def test_solve():
	assert solve('()()') is True
	assert solve('()') is True
	assert solve('((()') is False
	assert solve(')') is False
	assert solve('(())') is True
	assert solve('(()*') is True
	assert solve('(*)') is True
	assert solve(')*(') is False
