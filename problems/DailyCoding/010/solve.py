import time
import threading


from typing import Any, Callable, List



def solve(f: Callable[[], Any], n: int) -> None:
	threading.Timer(n / 1000, f).start()


def test_solve():
	memory: List[float] = []
	def function():
		memory.append(int(time.time() / 10))

	for delay in (10, 100, 1000, 2500):
		memory = []
		solve(function, delay)
		assert memory == []
		time.sleep((delay - (delay / 10)) / 1000)
		assert memory == []
		time.sleep((delay / 10) / 1000)
		assert memory == [int(time.time() / 10)]