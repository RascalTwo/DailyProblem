from typing import Any, List



def solve(a: List[Any], b: List[Any]) -> bool:
	return set(a) == set(b)


def test_solve():
	assert solve(['a', 'b'], ['b', 'a']) == True
	assert solve([None, False], [False, None]) == True

	assert solve(['a', 5], ['b', 5]) == False
	assert solve(['a', 'b', 'c'], ['a', 'b']) == False
	assert solve(['a', 'b'], ['a', 'b', True]) == False
