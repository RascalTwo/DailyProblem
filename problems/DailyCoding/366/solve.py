import itertools



def solve(string: str):
	for possible in itertools.permutations(string):
		for i, char in enumerate(possible[:-1]):
			if char == possible[i + 1]:
				break
		else:
			return ''.join(possible)

	return None


def test_solve():
	assert solve('yyz') == 'yzy'
	assert solve('yyy') is None
