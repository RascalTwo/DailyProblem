import itertools

from typing import Iterable, List



def solve(string: str, words: List[str]) -> Iterable[int]:
	for combined in (''.join(combo) for combo in itertools.permutations(words)):
		index = -1
		while True:
			try:
				index = string.index(combined, index + 1)
				yield index
			except:
				break


def test_solve():
	assert sorted(list(solve('dogcatcatcodecatdog', ['cat', 'dog']))) == [0, 13]
	assert list(solve('barfoobazbitbyte', ['dog', 'cat'])) == []
