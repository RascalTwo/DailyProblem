def solve(k: int, s: str):
	longest = []

	for start in range(len(s)):
		distinct = []
		for i in range(start, len(s)):
			distinct.append(s[i])
			if len(set(distinct)) <= k:
				distinct.remove(s[i])
				break
		longest = distinct if len(distinct) > len(longest) else longest

	return ''.join(longest)


def test_solve():
	assert solve(2, "abcba") == "bcb"
	assert solve(3, "zabcbaz") == "abcba"
