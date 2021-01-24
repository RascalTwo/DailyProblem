from typing import Callable, List



def test_solve():
	functions: List[Callable[..., int]] = []
	for i in range(10):
		functions.append(lambda : i)
	assert [f() for f in functions] == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]


	functions.clear()
	for i in range(10):
		functions.append(lambda i=i: i)
	assert [f() for f in functions] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


	functions.clear()
	for i in range(10):
		functions.append((lambda i: lambda: i)(i))
	assert [f() for f in functions] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
