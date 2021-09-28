from typing import Iterable, List



def solve(expression: List[str]) -> Iterable[List[str]]:
	for i in range(0, len(expression) - 2, 2):
		for j in range(i + 2, len(expression), 2):
			if not i and j == len(expression) - 1:
				continue

			new_exp = expression.copy()
			new_exp.insert(j + 1, ')')
			new_exp.insert(i, '(')
			yield new_exp


def test_solve():
	assert list(solve(['F', '|', 'T', '&', 'T'])) == [
		['(', 'F', '|', 'T', ')', '&', 'T'],
		['F', '|', '(', 'T', '&', 'T', ')'],
	]
