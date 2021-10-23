import itertools

from typing import Dict



def solve(expression: str):
	variables: Dict[str, bool] = {}
	for char in expression:
		if char.isalpha() and char.islower():
			variables[char] = True

	editing_expression = list(expression.replace('AND', 'and').replace('OR', 'or'))
	for o, char in enumerate(reversed(editing_expression)):
		if char != '¬':
			continue

		i = len(editing_expression) - o - 1
		next_char = editing_expression[i + 1]
		if not next_char.isalpha():
			continue

		del editing_expression[i]
		del editing_expression[i]
		editing_expression.insert(i, '')
		editing_expression.insert(i, f'(not {next_char})')
	expression = ''.join(editing_expression)

	for values in itertools.product([True, False], repeat=len(variables)):
		if eval(expression, {}, attempt := { key: values[i] for i, key in enumerate(variables.keys()) }):
			return attempt

	return False


def test_solve():
	assert solve('(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)') == {
		'a': False,
		'b': True,
		'c': True
	}
	assert solve('a AND b AND ¬a') == False
