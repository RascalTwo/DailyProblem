from typing import Iterable



def solve(word: str, string: str) -> Iterable[int]:
	search_chars = set(word)
	for i in range(len(string) - len(word) + 1):
		if set(string[i:i + len(word)]) == search_chars:
			yield i


def test_solve():
	assert list(solve('ab', 'abxaba')) == [0, 3, 4]
