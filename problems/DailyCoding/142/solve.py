def solve_recur(string: str, opened: int = 0) -> bool:
	for i, char in enumerate(string):
		if char == '*':
			if any(solve_recur(sub + string[i + 1:], opened) for sub in ' ()'):
				return True
		elif char == '(':
			opened += 1
		elif char == ')':
			if not opened:
				return False
			opened -= 1

	return not opened


def is_balanced(string: str) -> bool:
	opened = 0
	for char in string:
		if char == '(':
			opened += 1
		elif char == ')':
			if not opened:
				return False
			opened -= 1

	return not opened


def solve_iter(string: str) -> bool:
	if not '*' in string:
		return is_balanced(string)

	start = string.index('*')
	possibles = [string[:start]]

	for char in string[start:]:
		possibles = (
			[possible + sub for sub in ' ()' for possible in possibles]
			if char == '*' else
			[path + char for path in possibles]
		)

	return any(is_balanced(possible) for possible in possibles)


def test_solve():
	for solve in (solve_recur, solve_iter):
		assert solve('()()') is True
		assert solve('()') is True
		assert solve('((()') is False
		assert solve(')') is False
		assert solve('(())') is True
		assert solve('(()*') is True
		assert solve('(*)') is True
		assert solve(')*(') is False
		assert solve('(**') is True
		assert solve('((**') is True
		assert solve('()**') is True
		assert solve('((*)(') is False
		assert solve('((*') is False
