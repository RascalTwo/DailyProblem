from typing import Dict, Iterable, List, Union



def solve(mapping: Dict[Union[str, int], List[str]], digits: str) -> Iterable[str]:
	digit, remaining = digits[0], digits[1:]
	for char in mapping.get(int(digit), mapping.get(str(digit), [])):
		for suffix in solve(mapping, remaining) if remaining else ['']:
			yield char + suffix


def test_solve():
	assert list(solve({'2': ['a', 'b', 'c'], 3: ['d', 'e', 'f']}, '23')) == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
