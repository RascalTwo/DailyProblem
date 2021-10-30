from typing import Callable, List, Sequence, TypeVar, Union

T = TypeVar('T')
R = TypeVar('R')

Number = Union[int, float]



def reduce(array: Sequence[T], combine: Callable[[R, T], R], initial: R) -> R:
	value = initial
	for element in array:
		value = combine(value, element)
	return value


def test_solve():
	def add(a: Number, b: Number) -> Number:
		return a + b

	def sum(lst: List[Number]) -> Number:
		return reduce(lst, add, 0)
	assert sum([1, 2, 3, 4, 5]) == 15
