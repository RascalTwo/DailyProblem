import collections



def solve(string: str) -> str:
	frequencies = collections.defaultdict(int)
	for char in string:
		frequencies[char] += 1
	return ''.join(sorted(string, key = lambda char: (frequencies[char], char), reverse=True))


def test_solve():
	assert solve('tweet') == 'tteew'
