def solve(s1: str, s2: str) -> bool:
	return len(set(s1)) == len(set(s2))


def test_solve():
	assert solve('abc', 'bcd') is True
	assert solve('foo', 'bar') is False
