def solve(sample: str) -> bool:
	length = len(sample)
	if length < 2:
		return False
	if not sample[0].isalpha() or sample[0].islower():
		return False
	if not sample[1].isspace() and not sample[1].islower():
		return False

	for i, c in enumerate(sample[2:], 2):
		if c.isspace():
			if sample[i - 1].isspace():
				return False
		elif not c.isalpha() and c not in ',;:':
			if i != len(sample) - 1:
				return False
	if sample[-1] not in '.?!‽':
		return False

	return True


def test_solve():
	assert solve('Hello, world!') is True
	assert solve('HEllo, world!') is False
	assert solve(' A') is False
	assert solve('1 ') is False
	assert solve('a bird.') is False
	assert solve('A bird.') is True
	assert solve('A bird') is False
	assert solve('A bird  that flies.') is False
	assert solve('A bird; that flies.') is True
