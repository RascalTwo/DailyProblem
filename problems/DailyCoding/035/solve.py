from typing import List



def solve(characters: List[str], order: List[str]) -> List[str]:
	characters.sort(key = lambda c: order.index(c))
	return characters


def test_solve():
	assert solve(['G', 'B', 'R', 'R', 'B', 'R', 'G'], ['R', 'G', 'B']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
