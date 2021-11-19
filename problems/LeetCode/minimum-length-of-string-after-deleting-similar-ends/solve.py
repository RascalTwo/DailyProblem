def solve(target: str) -> int:
	while True:
		length = len(target)

		prefix = 0
		suffix = length - 1
		if not length or prefix == suffix or target[prefix] != target[suffix]:
			return length

		for i, char in enumerate(target[1:], 1):
			if char == target[prefix] and i != suffix:
				prefix = i
			else:
				break
		for i in range(length - 2, -1, -1):
			if target[i] == target[suffix] and i != prefix:
				suffix = i
			else:
				break
		target = target[prefix + 1:suffix]


def test_solve():
	assert solve('ca') == 2
	assert solve('cabaabac') == 0
	assert solve('aabccabba') == 3
	assert solve('bab') == 1
	assert solve('a') == 1
