def solve_reversed(string: str) -> str:
	return ''.join(reversed(string))


def solve_slice(string: str) -> str:
	return string[::-1]


def solve_iter(string: str) -> str:
	output = ''
	for char in string:
		output = char + output
	return output


def solve_half(string: str) -> str:
	length = len(string)
	output = list(string)

	for i in range(length // 2):
		j = length - 1 - i
		output[i], output[j] = output[j], output[i]

	return ''.join(output)


def test_solve():
	for solve in (solve_reversed, solve_slice, solve_iter, solve_half):
		assert solve('Hello, world!') == '!dlrow ,olleH'
		assert solve('abcd') == 'dcba'
		assert solve('12345') == '54321'
