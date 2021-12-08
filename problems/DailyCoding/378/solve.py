from typing import Any, List



def solve(data: Any) -> str:
	if data is None:
		return 'null'
	if isinstance(data, list):
		return '[' + ', '.join(map(solve, data)) + ']'
	if isinstance(data, dict):
		pairs: List[str] = []
		for key, value in data.items():
			pairs.append(f'"{key}": {solve(value)}')
		return '{' + ', '.join(pairs) + '}'
	if isinstance(data, str):
		return f'"{data}"'
	return str(data)


def test_solve():
	assert solve([None, 123, ["a", "b"], {"c":"d"}]) == '[null, 123, ["a", "b"], {"c": "d"}]'
