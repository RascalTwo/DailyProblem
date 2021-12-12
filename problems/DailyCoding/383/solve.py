from typing import List



def solve(string: str, *substrings: str) -> str:
	bolding: List[int] = []
	for start in range(len(string) - min(map(len, substrings)) + 1):
		for substring in substrings:
			length = len(substring)
			if substring == string[start:start + length]:
				bolding += list(range(start, start + length))

	ranges: List[List[int]] = []
	current = [bolding[0], bolding[0]]
	for i in bolding[1:]:
		if abs(i - current[1]) <= 1:
			current[1] = i
		else:
			ranges.append(current)
			current = [i, i]
	ranges.append(current)

	result = list(string)
	for first, last in ranges[::-1]:
		result.insert(last + 1, '</b>')
		result.insert(first, '<b>')
	return ''.join(result)


def test_solve():
	assert solve('abcdefg', 'bc', 'ef') == 'a<b>bc</b>d<b>ef</b>g'
	assert solve('abcdefg', 'bcd', 'def') == 'a<b>bcdef</b>g'
	assert solve('abcdefg', 'bcd', 'ef') == 'a<b>bcdef</b>g'
