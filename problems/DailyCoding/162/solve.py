import collections


from typing import Any, DefaultDict, Iterable



def solve(*words: str) -> Iterable[str]:
	root: DefaultDict[str, Any] = collections.defaultdict(dict)
	for word in words:
		current = root
		for char in word:
			current = current.setdefault(char, collections.defaultdict(dict))

	for word in words:
		path = [root]
		for char in word:
			path.append(path[-1][char])

		j = len(path) - 2
		for i, node in enumerate(path[::-1]):
			if len(node) > 1:
				break
			j = len(path) - 1 - i - 1
		yield word[:j + 1]


def test_solve():
	assert list(solve('dog', 'cat', 'apple', 'apricot', 'fish')) == ['d', 'c', 'app', 'apr', 'f']
