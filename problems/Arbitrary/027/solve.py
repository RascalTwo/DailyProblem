import collections



def solve(letter: str, newspaper: str) -> bool:
	counts = collections.Counter(newspaper)
	need_counts = collections.Counter(letter)
	return not any(counts[char] < count for char, count in need_counts.items())


def test_solve():
	assert solve('abc', 'euokdcba') is True
	assert solve('abc', 'aabbcc') is True
	assert solve('hello world!', ' !dehllloorw') is True
	assert solve('hello world!', ' abc') is False
