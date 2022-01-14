def solve(string: str) -> int:
	leading_space = 0
	for char in string:
		if char == ' ':
			leading_space += 1
		else:
			break
	string = string[leading_space:]
	if not string:
		return 0

	sign = -1 if string[0] == '-' else 1
	if string[0] in '+-':
		string = string[1:]

	value = 0
	for char in string:
		if char.isdigit():
			value = (value * 10) + int(char)
		else:
			break

	return max(min(value * sign, 2147483647), -2147483648)



def test_solve():
	assert solve('42') == 42
	assert solve(' -42') == -42
	assert solve('4193 with words') == 4193
