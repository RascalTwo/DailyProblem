from typing import Dict, List, Optional, Tuple, Union, Literal

Rule = Union[Literal['>'], Literal['<']]



def solve(lines: List[int]):
	values: Dict[int, int] = {}
	rules: Dict[int, Tuple[Optional[Rule], Optional[Rule]]] = {}
	for i, a in enumerate(lines):
		values[i] = 1
		before = ('<' if a > lines[i - 1] else '>') if i else None
		after = ('>' if a > lines[i + 1] else '<') if i + 1 <= len(lines) - 1 else None
		if before is not None and after is not None:
			rules[i] = before, after

	while True:
		original = list(values.values())

		for j in values.keys():
			if j not in rules:
				continue
			before, after = rules[j]
			i, k = j - 1, j + 1

			if before == '<' and after == '<':
				values[j] = values[i] + 1
				values[k] = values[i] + 2
			elif before == '<' and after == '>':
				values[k] = values[i]
				values[j] = values[i] + 1
			elif before == '>' and after == '>':
				values[j] = values[i] - 1
				values[k] = values[i] - 2
			elif before == '>' and after == '<':
				values[k] = values[i]
				values[j] = values[i] - 1

		if original == list(values.values()):
			break

	return original


def test_solve():
	assert solve([10, 40, 200, 1000, 60, 30]) == [1, 2, 3, 4, 3, 2]
