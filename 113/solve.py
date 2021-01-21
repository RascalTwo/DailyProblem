from typing import List



def solve(words: str) -> List[str]:
	return words.split()[::-1]


def test_solve():
	assert solve('here world here') == ['here', 'world', 'here']
	assert solve('one  two   three') == ['three', 'two', 'one']
