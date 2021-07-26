import itertools

from typing import Dict



def solve(one: str, two: str, result: str) -> Dict[str, int]:
	def str_to_num(string: str) -> int:
		return int(''.join(mapping[char] for char in string))

	non_zeros = set([one[0], two[0], result[0]])
	characters = list(set([*one, *two, *result]))
	for assignment in itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], len(characters)):
		mapping = dict(zip(characters, assignment))
		if any(char in non_zeros and value == '0' for char, value in mapping.items()):
			continue
		if str_to_num(one) + str_to_num(two) == str_to_num(result):
			return {char: int(value) for char, value in mapping.items()}

	return {}


def test_solve():
	assert solve('send', 'more', 'money') == {'s': 9, 'e': 5, 'n': 6, 'd': 7, 'm': 1, 'o': 0, 'r': 8, 'y': 2}
