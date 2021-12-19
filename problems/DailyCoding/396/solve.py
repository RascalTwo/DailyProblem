import itertools
import collections



def is_palindromic(string: str):
	return sum(1 for count in collections.Counter(string).values() if count % 2) <= 1


def solve(string: str):
	return max(
		len(subsequence)
		for length in range(len(string) - 1, -1, -1)
		for subsequence in set(itertools.combinations(string, r=length))
		if is_palindromic(''.join(subsequence))
	)


def test_solve():
	assert solve('MAPTPTMTPA') == 9
