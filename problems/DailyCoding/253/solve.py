from typing import List



def solve(string: str, k: int) -> List[str]:
	lines: List[List[str]] = [[' ' for _ in range(len(string))] for _ in range(k)]

	i = 0
	while i != len(string):
		for r in range(min(k, len(string) - i)):
			lines[r][i] = string[i]
			i += 1

		for r in range(k-2, 0, -1):
			if i == len(string):
				break
			lines[r][i] = string[i]
			i += 1

	return [''.join(line) for line in lines]


def test_solve():
	assert solve('thisisazigzag', 4) == [
		't     a     g',
    ' h   s z   a ',
    '  i i   i z  ',
    '   s     g   '
	]
	assert solve('thisisazigzag', 3) == [
		't   i   i   g',
    ' h s s z g a ',
    '  i   a   z  '
	]
	assert solve('thisisazigzagy', 5) == [
		't       i     ',
    ' h     z g    ',
    '  i   a   z   ',
		'   s s     a y',
		'    i       g '
	]