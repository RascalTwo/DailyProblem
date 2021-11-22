def solve(jewels: str, stones: str):
	jewel_set = set(jewels)
	return sum(1 for stone in stones if stone in jewel_set)


def test_solve():
	assert solve('z', 'ZZ') ==  0
	assert solve('aA', 'aAAbbbb') ==  3
