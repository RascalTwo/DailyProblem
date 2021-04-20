from typing import List, Tuple



def solve(string: str) -> str:
	stack: List[Tuple[str, int]] = []
	multiple = 0

	result = ''
	for char in string:
		if char.isdigit():
			multiple = multiple * 10 + int(char)
		elif char == '[':
			stack.append((result, multiple))
			result, multiple = '', 0
		elif char == ']':
			prev, prev_multiple = stack.pop()
			result = prev + (result * prev_multiple)
		else:
			result += char

	return result


def test_solve():
	assert solve('3[a]2[bc]') == 'aaabcbc'
	assert solve('2[abc]3[cd]ef') == 'abcabccdcdcdef'
	assert solve('11[ab]rft3[brf]') == 'abababababababababababrftbrfbrfbrf'
	assert solve('3[a2[c]]') == 'accaccacc'
	assert solve('2[a2[b2[cd]]]') == 'abcdcdbcdcdabcdcdbcdcd'
