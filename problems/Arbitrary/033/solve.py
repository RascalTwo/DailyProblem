def solve(goal: str, lyric: str) -> bool:
	found = 0
	for word in lyric.split(' '):
		if goal[found] not in word:
			continue
		found += 1

		if found == len(goal):
			return True

	return found == len(goal)


def test_solve():
	assert solve('boom', 'everybody\'s looking for something"') is True
	assert solve('abc', 'everybody\'s looking for something"') is False
	assert solve('toe', 'It\'s the eye of the tiger') is True
