from typing import Optional, Set



def solve(string: str) -> Optional[str]:
	seen: Set[str] = set()

	for char in string:
		if char in seen:
			return char
		seen.add(char)


def test_solve():
	assert solve('acbbac') == 'b'
	assert solve('abcdef') == None
