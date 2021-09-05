import sys

from typing import List



POSSIBLES = set('RGB')

def solve(quxes: List[str]) -> int:
	completed: List[List[List[str]]] = []

	processing: List[List[List[str]]] = [[]]
	while processing:
		branches: List[List[str]] = []

		path = processing.pop()
		latest = path[-1] if path else quxes
		for i, c in enumerate(latest[:-1]):
			if latest[i + 1] == c:
				continue
			branch = latest[:]
			branch[i:i + 2] = next(iter(POSSIBLES - set([c, latest[i + 1]])))
			branches.append(branch)

		for branch in branches:
			processing.append([*path, branch])
		if not branches:
			completed.append(path)

	least = sys.maxsize
	count = 0
	for path in completed:
		length = len(path[-1])
		if length < least:
			least = length
			count = 1
		elif length == least:
			count += 1

	return count


def test_solve():
	assert solve(['R', 'G', 'B', 'G', 'B']) == 10
