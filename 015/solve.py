import random
import statistics


from typing import DefaultDict, Iterable, TypeVar



T = TypeVar('T')


def solve(stream: Iterable[T]) -> T:
	chosen = None
	for i, element in enumerate(stream):
		if i == 0 or not random.randrange(i):
			chosen = element

	assert chosen
	return chosen


def test_solve():
	assert statistics.median((solve(range(100)) for _ in range(10000))) == 50.0


