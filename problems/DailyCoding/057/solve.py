def solve(s: str, k: int):
	lines = []
	line = []

	for word in s.split(' '):
		if len(' '.join(line + [word])) <= k:
			line.append(word)
			continue

		if not line:
			return None
		lines.append(' '.join(line))
		line = [word]

	return lines + [' '.join(line)] if line else lines


def test_solve():
	assert solve("the quick brown fox jumps over the lazy dog", 10) == ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
	assert solve('amazing world', 3) is None
