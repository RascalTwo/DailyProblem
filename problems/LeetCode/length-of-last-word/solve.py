def solve(string: str) -> int:
	for e in range(len(string) - 1, -1, -1):
		if string[e].isspace():
			continue
		for s in range(e, -1, -1):
			if string[s].isspace():
				return e - s
		return e + 1
	return 0


def test_solve():
	assert solve('Hello World') == 5
	assert solve('   fly me   to   the moon  ') == 4
	assert solve('luffy is still joyboy') == 6
	assert solve('a') == 1
	assert solve('bird') == 4
