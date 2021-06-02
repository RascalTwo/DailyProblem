from typing import Any, List, Sequence



def solve(a: str, b: str, c: str):
	a_len = len(a) + 1
	b_len = len(b) + 1
	c_len = len(c) + 1
	longests = [
		[
			[0 for _ in range(c_len)]
			for _ in range(b_len)
		]
		for _ in range(a_len)
	]

	for i in range(a_len):
		for j in range(b_len):
			for k in range(c_len):
				if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
					longests[i][j][k] = longests[i - 1][j - 1][k - 1] + 1
				else:
					longests[i][j][k] = max(longests[i - 1][j][k], longests[i][j - 1][k], longests[i][j][k - 1])

	return longests[a_len - 2][b_len - 2][c_len - 2]


def test_solve():
	assert solve('abc', 'abc', 'abc') == 3
	assert solve('a', 'bc', 'def') == 0
	assert solve('abc', 'ac', 'bc') == 1
	assert solve('epidemiologist', 'refrigeration', 'supercalifragilisticexpialodocious') == 5
