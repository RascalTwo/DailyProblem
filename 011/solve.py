import collections


from typing import Callable, DefaultDict, Iterable, List, Tuple




InfiniteDict = DefaultDict[str, Tuple['InfiniteDict', bool]]


def solve(query: str, strings: List[str]) -> List[str]:
	infinite_dict: Callable[[], InfiniteDict] = lambda: collections.defaultdict(lambda: (infinite_dict(), False))


	trie: InfiniteDict = infinite_dict()
	for string in strings:
		current = trie
		for char in string[:-1]:
			current = current[char][0]

		char = string[-1]
		current[char] = (current[char][0], True)

	def collect(prefix: str, current: InfiniteDict) -> Iterable[str]:
		for next_char, (next_chars, is_word) in current.items():
			new_prefix = prefix + next_char
			if is_word:
				yield new_prefix
			yield from collect(new_prefix, next_chars)

	current = trie
	for char in query:
		current = current[char][0]

	return list(collect(query, current))


def test_solve():
	assert solve('de', ['dog', 'deer', 'deal']) == ['deer', 'deal']
	assert solve('he', ['hello world', 'hi', 'hello', 'hell', 'head', 'universe']) == ['hell', 'hello', 'hello world', 'head']
test_solve()