import itertools

from typing import Dict, Iterable, List, Set, Tuple



def find_possible_paths(r: int, c: int, word: str, matrix: List[List[str]]) -> Iterable[List[Tuple[int, int]]]:
	if r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[r]):
		return

	if matrix[r][c] != word[0]:
		return

	if len(word) == 1:
		yield [(r, c)]
		return

	# Up, Down, Left, Right
	for neighbor in ((r - 1, c), (r,  c - 1), (r + 1, c), (r, c + 1)):
		for path in find_possible_paths(*neighbor, word[1:], matrix):
			yield [(r, c), *path]


def solve(words: Set[str], matrix: List[List[str]]) -> Set[str]:
	word_paths: Dict[str, List[List[Tuple[int, int]]]] = {}
	for word in words:
		for r, row in enumerate(matrix):
			for c, char in enumerate(row):
				if word.startswith(char):
					word_paths.setdefault(word, []).extend(find_possible_paths(r, c, word, matrix))

	for desired in range(len(words) - 1, 0, -1):
		for combo in itertools.combinations(words, r=desired):
			for paths in itertools.product(*(word_paths[word] for word in combo)):
				if len(flattened := list(itertools.chain(*paths))) == len(set(flattened)):
					return set(combo)


def test_solve():
	assert solve({ 'eat', 'rain', 'in', 'rat' }, [
		['e', 'a', 'n'],
		['t', 't', 'i'],
		['a', 'r', 'a']
	]) == { 'eat', 'in', 'rat' }
	assert solve({ 'eat', 'rain', 'in', 'rat', 'pat' }, [
		['e', 'a', 'n', '0'],
		['t', 't', 'i', '0'],
		['a', 'r', 'a', '0'],
		['p', '0', 't', '0'],
	]) == { 'eat', 'in', 'rat', 'pat' }
