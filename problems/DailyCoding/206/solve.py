from typing import List



def solve(chars: List[str], locations: List[int]) -> List[str]:
	return [chars[i] for i in locations]


def test_solve():
	assert solve(['a', 'b', 'c'], [2, 1, 0]) == ['c', 'b', 'a']
	assert solve(['d', 'a', 'c', 'b'], [1, 3, 2, 0]) == ['a', 'b', 'c', 'd']
