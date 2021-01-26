def solve(string: str) -> bool:
	return len(set(string)) == len(string)


def test_solve():
	assert solve('isogram') is True
	assert solve('heterogram') is False
