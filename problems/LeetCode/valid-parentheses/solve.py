from typing import Sequence, Tuple


def solve(string: str, pairs: Sequence[Tuple[str, str]]=[('(', ')'), ('[', ']'), ('{', '}')]) -> bool:
	openings = [pair[0] for pair in pairs]
	closings = [pair[1] for pair in pairs]
	stack = []
	for char in string:
		if char in openings:
			stack.append(char)
		elif char in closings:
			if not stack or openings[closings.index(char)] != stack.pop(-1):
				return False

	return not stack



def test_solve():
	assert solve('([])[]({})') is True
	assert solve('([)]') is False
	assert solve('((()') is False
	assert solve(')') is False
