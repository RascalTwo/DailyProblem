import itertools

from typing import List



def solve(*histories: List[str]) -> List[str]:
	return max((
		first
		for first, *rest in itertools.product(*(
			[history[i:j] for i in range(len(history)) for j in range(i + 1, len(history) + 1)]
			for history in histories
		))
		if all(path == first for path in rest)
	), key = lambda path: len(path))



def test_solve():
	assert solve(['/home', '/register', '/login', '/user', '/one', '/two'], ['/home', '/red', '/login', '/user', '/one', '/pink']) == ['/login', '/user', '/one']
