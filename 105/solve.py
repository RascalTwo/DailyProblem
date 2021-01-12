import time

from typing import Any, Callable, List



def solve(f: Callable[..., Any], n: int) -> Callable[..., Any]:
	called = 0
	def wrapper(*args: Any, **kwargs: Any):
		nonlocal called
		diff = time.time() - called
		if diff < n:
			time.sleep(n / 1000)
		called = time.time()
		return f(*args, **kwargs)
	return wrapper


def test_solve():
	add_to_list: Callable[[List[int]], None] = lambda b: b.append(len(b))

	a: List[int] = []

	debounced = solve(add_to_list, 1000)
	debounced(a)
	assert a == [0]
	debounced(a)
	assert a == [0, 1]
	debounced(a)
	assert a == [0, 1, 2]
