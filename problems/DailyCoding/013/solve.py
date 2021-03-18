from typing import List



def solve(s: str, k: int):
	longest = []

	for start in range(len(s)):
		distinct: List[str] = []
		for i in range(start, len(s)):
			distinct.append(s[i])
			if len(set(distinct)) > k:
				distinct.remove(s[i])
				break
		longest = distinct if len(distinct) > len(longest) else longest

	return ''.join(longest)


def test_solve():
	assert solve("abcba", 2) == "bcb"
	assert solve("zabcbaz", 3) == "abcba"
