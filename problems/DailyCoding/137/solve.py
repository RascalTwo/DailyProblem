from typing import Any



class BitArray:
	def __init__(self):
		self.value = 0


	def __getitem__(self, key: Any):
		if not isinstance(key, int):
			raise KeyError('key must be an integer')
		return (self.value >> key) & 1


	def __setitem__(self, key: Any, value: Any):
		if not isinstance(key, int) or not isinstance(value, int):
			raise ValueError('key and value must be integers')

		mask = 1 << key
		self.value = (self.value | mask) if value else self.value & ~mask


def test_solve():
	ba = BitArray()
	ba[0] = 1
	assert ba[0]

	ba[2] = 1
	assert ba[0] and ba[2]

	ba[2] = 0
	assert ba[0] and not ba[2]
