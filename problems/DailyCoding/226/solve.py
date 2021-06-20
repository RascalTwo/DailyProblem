import collections

from typing import DefaultDict, Dict, List, Set


def solve(words: List[str]) -> List[str]:
	rules: DefaultDict[str, Set[str]] = collections.defaultdict(set)
	for i, word in enumerate(words):
		for other in words[i + 1:]:
			for ci in range(min(len(word), len(other))):
				w, o = word[ci], other[ci]
				if w != o:
					rules[w].add(o)
					break

	values: Dict[str, int] = {}
	for key, chars in rules.items():
		for char in (key, *chars):
			if char not in values:
				values[char] = len(values) * 100

	while True:
		for first_char, later_chars in rules.items():
			first_value = values[first_char]
			later_values = [values[l] for l in later_chars]
			if any(first_value > lv for lv in later_values):
				least = min(later_values)
				values[first_char] = least - 1
				break
		else:
			break

	return [char for char, _ in sorted(values.items(), key=lambda pair: pair[1])]


def test_solve():
	assert solve(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']) == ['x', 'z', 'w', 'y']