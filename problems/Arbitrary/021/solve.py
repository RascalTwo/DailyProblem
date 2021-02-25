import collections


from typing import DefaultDict, Dict, List



def solve(string: str) -> Dict[str, List[int]]:
	counts: DefaultDict[str, List[int]] = collections.defaultdict(list)
	for i, char in enumerate(string):
		counts[char].append(i)
	return counts


def test_solve():
	assert solve('abc  cba') == {'a': [0, 7], 'b': [1, 6], 'c': [2, 5], ' ': [3, 4]}

	assert solve('hello, world!') == {'h': [0], 'e': [1], 'l': [2, 3, 10], 'o': [4, 8], ',': [5], ' ': [6], 'w': [7], 'r': [9], 'd': [11], '!': [12]}
