def solve(parentheses: str) -> int:
	opens = 0
	closes = 0
	for char in parentheses:
		if char == '(':
			opens += 1
		elif char == ')':
			if opens:
				opens -= 1
			else:
				closes += 1


	return abs(opens) + closes


def test_solve():
	assert solve('()())()') == 1
	assert solve(')(') == 2
	assert solve(')()') == 1
	assert solve(')(((') == 4
	assert solve(')())(') == 3
