from typing import Dict, Iterable, Tuple



def merge_iterators(*raw_iterators: Iterable[int]) -> Iterable[int]:
	values: Dict[int, Tuple[int, Iterable[int]]] = {
		i: (next(iterator), iterator) for i, iterator in enumerate(raw_iterators)
	}
	while values:
		i, (value, iterator) = sorted([(i, value) for i, value in values.items()], key = lambda item: item[1][0])[0]
		yield value
		try:
			values[i] = (next(iterator), iterator)
		except:
			del values[i]


def test_solve():
	assert list(merge_iterators(iter([5, 10, 15]), iter([3, 8, 9]))) == [3, 5, 8, 9, 10, 15]
	assert list(merge_iterators(iter([5, 10, 15]), iter([3, 8, 9]), iter([0, 12]))) == [0, 3, 5, 8, 9, 10, 12, 15]
