from typing import Dict



class KVS:
	def __init__(self):
		self.data: Dict[int, int] = {}

	def update(self, key: int, val: int):
		self.data[key] = val

	def get(self, key: int):
		return self.data.get(key, None)

	def max_key(self, val: int):
		return max(key for key, lval in self.data.items() if lval == val)


def test_solve():
	kv = KVS()
	kv.update(1, 1)
	kv.update(2, 1)
	assert kv.max_key(1) == 2
