import itertools

from typing import Iterable


def solve(string: str) -> Iterable[str]:
	for length in range(1, len(string) + 1):
		yield from (''.join(combo) for combo in itertools.combinations(string, r=length))


def test_solve():
	assert list(solve('xyz')) == ['x', 'y', 'z', 'xy', 'xz', 'yz', 'xyz']
