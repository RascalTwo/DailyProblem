from typing import List



def solve(path: str):
	location: List[str] = []

	for directory in path.split('/')[1:-1]:
		if directory == '..':
			location.pop()
		elif directory != '.':
			location.append(directory)

	return '/' + '/'.join(location) + '/'


def test_solve():
	assert solve('/usr/bin/../bin/./scripts/../') == '/usr/bin/'
