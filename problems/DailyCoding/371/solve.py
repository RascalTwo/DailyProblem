from typing import Dict, List, Tuple



def solve(text: str):
	dependants: Dict[int, List[str]] = {}
	expressions: List[Tuple[List[str], List[str]]] = []
	for i, line in enumerate(text.strip().split('\n')):
		left, right = line.split(' = ')
		tokens = [left] + right.split(' + ')
		variables = [token for token in tokens if token.isalpha()]
		expressions.append((tokens, variables))

		for variable in variables:
			dependants.setdefault(i, []).append(variable)


	values: Dict[str, int] = {}

	while dependants:
		index = min(dependants.keys(), key = lambda i: len(dependants[i]))
		(expected, *additions), variables = expressions[index]
		del dependants[index]
		values[next(variable for variable in variables if variable not in values)] = int(expected) - sum(map(int, [token if token.isdigit() else values.get(token, 0) for token in additions])) if expected.isdigit() else sum(map(int, [token if token.isdigit() else values[token] for token in additions]))

	return values


def test_solve():
	assert solve('y = x + 1\n5 = x + 3\n10 = z + y + 2') == { 'x': 2, 'y': 3, 'z': 5 }
