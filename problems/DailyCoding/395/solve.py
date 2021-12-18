from typing import Dict, List



def solve(strings: List[str]) -> List[List[str]]:
	groups: Dict[str, List[str]] = {}
	for string in strings:
		chars = set(string)
		groups.setdefault(''.join(sorted(chars)), []).append(string)
	return list(groups.values())


def test_solve():
	assert solve(['eat', 'ate', 'apt', 'pat', 'tea', 'now']) == [['eat', 'ate', 'tea'], ['apt', 'pat'], ['now']]
