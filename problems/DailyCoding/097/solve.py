from typing import Optional



class TimeMap:
	def __init__(self):
		self.map = {}

	def clear(self):
		self.map.clear()

	def set(self, key: int, value: int, time: int):
		self.map.setdefault(key, {})[time] = value

	def get(self, key: int, time: int) -> Optional[int]:
		return next((value for vtime, value in reversed(self.map.get(key, {}).items()) if vtime <= time), None)


def test_solve():
	d = TimeMap()

	d.set(1, 1, 0) # set key 1 to value 1 at time 0
	d.set(1, 2, 2) # set key 1 to value 2 at time 2
	assert d.get(1, 1) == 1
	assert d.get(1, 3) == 2
	d.clear()


	d.set(1, 1, 5) # set key 1 to value 1 at time 5
	assert d.get(1, 0) == None
	assert d.get(1, 10) == 1


	d.clear()
	d.set(1, 1, 0) # set key 1 to value 1 at time 0
	d.set(1, 2, 0) # set key 1 to value 2 at time 0
	assert d.get(1, 0) == 2
