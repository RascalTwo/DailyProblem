from typing import Dict, List, Set



def solve(string: str, delimiters: Set[str]) -> str:
	delims: Dict[int, str] = {}
	for i in range(len(string)):
		char = string[i]
		if char in delimiters:
			delims[i] = char
	if len(string) not in delims:
		delims[len(string)] = ''

	words: List[str] = []
	for i, index in enumerate(delims):
		first_index = 0 if not i else list(delims)[i-1]+1
		words.append(string[first_index:index])

	if not words[-1]:
		words.pop(-1)

	combined = ''
	for i, word in enumerate(words[::-1]):
		combined += word + list(delims.values())[i]
	return combined


def test_solve():
	assert solve('hello/world:here', {'/', ':'}) == 'here/world:hello'
	assert solve('hello/world:here/', {'/', ':'}) == 'here/world:hello/'
	assert solve('hello//world:here', {'/', ':'}) == 'here/world/:hello'
