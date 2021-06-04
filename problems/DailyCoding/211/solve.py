from typing import List



def solve(haystack: str, needle: str) -> List[int]:
	needle_len = len(needle)

	indices: List[int] = []
	for start in range(len(haystack) - needle_len + 1):
		if haystack[start:start + needle_len] == needle:
			indices.append(start)

	return indices


def test_solve():
	assert solve('abracadabra', 'abr') == [0, 7]
	assert solve('abccbaabc', 'abc') == [0, 6]
