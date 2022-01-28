from typing import List



def solve(strings: List[str]) -> str:
	while len(strings) > 1:
		numbers: List[int] = []
		for string in (strings[0], strings[1]):
			value = 0
			for char in string:
				value = value * 10 + (ord(char) - 48)
			numbers.append(value)

			strings.pop(strings.index(string))

		str_result = ''
		result = numbers[0] * numbers[1]
		while result:
			result, digit = divmod(result, 10)
			str_result += chr(digit + 48)
		strings.append(str_result[::-1] or '0')

	return strings[0]


def test_solve():
	assert solve(['2', '3']) == '6'
	assert solve(['123', '456']) == '56088'
	assert solve(['1', '2', '3', '4', '5', '67', '890']) == '7155600'
	assert solve(['0', '0']) == '0'
