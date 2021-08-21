import heapq

from typing import List, Tuple, Union



AUTO_TOKENS = set('()')

OPERATOR_PRECEDENCES = {
	'^': 0,
	'/': 1,
	'*': 1,
	'-': 2,
	'+': 2
}

def perform_operation(left: float, operator: str, right: float) -> float:
	if operator == '^':
		return left ** right
	elif operator == '/':
		return left / right
	elif operator == '*':
		return left * right
	elif operator == '-':
		return left - right
	elif operator == '+':
		return left + right
	raise ValueError(f'Invalid operator passed: {operator}')


def evaluate(tokens: List[Union[float, str]]) -> float:
	left = 0
	right = len(tokens) - 1
	while True:
		if tokens[left] != '(':
			left += 1
		if tokens[right] != ')':
			right -= 1
		if tokens[left] == '(' and tokens[right] == ')':
			tokens[left:right + 1] = [evaluate(tokens[left + 1:right])]
			left = 0
			right = len(tokens) - 1
		if left >= right:
			break

	while len(tokens) > 1:
		queue: List[Tuple[int, int]] = []
		for i, char in enumerate(tokens):
			if char in OPERATOR_PRECEDENCES:
				assert isinstance(char, str)
				heapq.heappush(queue, (OPERATOR_PRECEDENCES[char], i))
		_, index = heapq.heappop(queue)
		left = tokens[index - 1]
		operator = tokens[index]
		right = tokens[index + 1]
		tokens[index-1:index+2] = [perform_operation(left, operator, right)]

	return tokens[0]


def solve(raw_expression: str) -> float:
	tokens: List[Union[float, str]] = []
	building: str = ''
	for char in raw_expression:
		if char == ' ':
			if building:
				tokens.append(building)
				building = ''
			continue
		if char in AUTO_TOKENS:
			if building:
				tokens.append(building)
				building = ''
			tokens.append(char)
			continue
		building += char
	if building:
		tokens.append(building)

	for i, token in enumerate(tokens):
		if token in AUTO_TOKENS or token in OPERATOR_PRECEDENCES:
			continue
		assert isinstance(token, str)

		negative = token.startswith('-')
		if negative:
			token = token[1:]

		result = 0
		for digit in token:
			result = (result * 10) + (ord(digit) - 48)
		tokens[i] = -result if negative else result

	return evaluate(tokens)


def test_solve():
	assert solve('-1 + (2 + 3)') == 4
	assert solve('1 + 5 * 2') == 11
	assert solve('(1 + 5) * 2') == 12
	assert solve('1 + (5 + (10 - 2))') == 14
