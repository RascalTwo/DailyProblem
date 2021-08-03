import itertools

from typing import Iterable, List, Literal, Union



def solve(relations: List[Union[None, Literal['+'], Literal['-']]]) -> Iterable[List[int]]:
	for permutation in itertools.permutations(list(range(len(relations)))):
		for i, change in enumerate(relations[1:], 1):
			if change == '+' and permutation[i-1] > permutation[i]:
				break
			elif change == '-' and permutation[i-1] < permutation[i]:
				break
		else:
			yield list(permutation)
	return []


def test_solve():
	assert [1, 2, 3, 0, 4] in solve([None, '+', '+', '-', '+'])
