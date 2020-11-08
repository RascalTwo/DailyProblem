from typing import MutableSequence


def solve(words: MutableSequence[str], string: str):
	used = []

	while string:
		word = next(word for word in words if string.startswith(word))
		words.remove(word)
		used.append(word)
		string = string[len(word):]

	return used


def test_solve():
	assert solve(['quick', 'brown', 'the', 'fox'], 'thequickbrownfox') == ['the', 'quick', 'brown', 'fox']
	assert solve(['bed', 'bath', 'bedbath', 'and', 'beyond'], 'bedbathandbeyond') in [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]
