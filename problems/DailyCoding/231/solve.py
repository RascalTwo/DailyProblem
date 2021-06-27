import collections


from typing import Optional


def solve(string: str) -> Optional[str]:
	counts = {}
	chars = list(string)
	i = 0
	while i != len(chars) - 2:
		j = i + 1
		char, other = chars[i], chars[j]

		if char not in counts:
			counts[char] = chars.count(char)
			if counts[char] > len(chars) // 2:
				return None

		i += 1

		if char != other:
			continue

		for k in range(j + 1, len(chars)):
			if chars[k] != char and (k == len(chars) - 1 or chars[k+1] != char):
				chars.insert(k + 1, char)
				i -= 1
				chars.pop(i)
				break
		else:
			return None

	return ''.join(chars)


def test_solve():
	assert solve('aaabbc') == 'ababac'
	assert solve('aaab') == None
