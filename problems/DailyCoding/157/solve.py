import collections



def solve(string: str) -> bool:
	return len([
		count
		for count in collections.Counter([
			char
				for char in string.lower()
				if char.strip()
		]).values()
		if count % 2 == 1
	]) <= 1


def test_solve():
	assert solve('carrace') is True
	assert solve('daily') is False
	assert solve('abccba') is True
	assert solve('abcdcba') is True
	assert solve('aaaabbbb') is True
	assert solve('abcdcb') is False
	assert solve('stats') is True
	assert solve('dog geese Do see') is True
