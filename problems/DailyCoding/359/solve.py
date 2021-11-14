import itertools

from typing import List


def solve(words: List[str], scrambled: str) -> int:
	characters = sorted(scrambled)
	for count in range(len(words) - 1, -1, -1):
		for combo in itertools.combinations(words, r=count):
			chars = []
			for word in combo:
				chars += list(word)

			if sorted(chars) != characters:
				continue

			result = 0
			for number in sorted([words.index(word) for word in combo]):
				result = (result * 10) + number
			return result


def test_solve():
	assert solve(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 'niesevehrtfeev') == 357
