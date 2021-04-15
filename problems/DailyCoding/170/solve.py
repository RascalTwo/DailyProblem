from typing import List, Optional



def get_differences(a: str, b: str):
	diffs = 0
	for i, char in enumerate(a):
		if b[i] != char:
			diffs += 1
	return diffs


def solve(start: str, end: str, dictionary: List[str]) -> Optional[List[str]]:
	reached: List[List[str]] = []

	paths: List[List[str]] = [[start]]
	while paths:
		path = paths.pop()
		current = path[-1]
		if current == end:
			reached.append(path)
			continue

		for word in dictionary:
			if word not in path and get_differences(current, word) == 1:
				paths.append(path + [word])


	best = None
	for path in reached:
		if best is None or len(path) < len(best):
			best = path
	return best


def test_solve():
	assert solve('dog', 'cat', ['dot', 'dop', 'dat', 'cat']) == ['dog', 'dot', 'dat', 'cat']
	assert solve('dog', 'cat', ['dot', 'tod', 'dat', 'dar']) == None

