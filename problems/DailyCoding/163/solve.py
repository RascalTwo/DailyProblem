from typing import Callable, Dict, List, Union

Number = Union[int, float]



OPERATORS: Dict[str, Callable[[Number, Number], Number]] = {
	'+': lambda a, b: a + b,
	'-': lambda a, b: a - b,
	'*': lambda a, b: a * b,
	'/': lambda a, b: a / b
}


def solve(expression: List[Union[str, int]]) -> Number:
	stack: List[Union[str, int, float]] = []
	for part in expression:
		if part not in OPERATORS:
			stack.append(part)
			continue

		b, a = stack.pop(), stack.pop()
		assert isinstance(part, str)
		assert isinstance(a, (int, float)) and isinstance(b, (int, float))

		stack.append(OPERATORS[part](a, b))

	result = stack.pop()
	assert isinstance(result, (int, float))
	return result


def test_solve():
	assert solve([5, 3, '+']) == 8
	assert solve([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']) == 5
