import functools


from typing import Callable, List



def test_solve():
	def make_functions():
		flist: List[Callable[[], int]] = []

		for i in [1, 2, 3]:
			def print_i(i: int):
				return i
			flist.append(functools.partial(print_i, i))

		return flist

	assert [f() for f in make_functions()] == [1, 2, 3]
