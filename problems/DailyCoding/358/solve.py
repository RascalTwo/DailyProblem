from typing import Dict



class Incrementor:
	def __init__(self):
		self.values: Dict[str, int] = {}

	def plus(self, key: str):
		if key not in self.values:
			self.values[key] = 0
		self.values[key] += 1

	def minus(self, key: str):
		if key not in self.values:
			return
		self.values[key] -= 1
		if not self.values[key]:
			del self.values[key]

	def get_max(self):
		return max(self.values.keys(), key = lambda key: self.values[key])

	def get_min(self):
		return min(self.values.keys(), key = lambda key: self.values[key])


def test_solve():
	instance = Incrementor()

	instance.plus('b')
	assert instance.get_max() == 'b'

	instance.plus('a')
	instance.plus('a')
	assert instance.get_max() == 'a'
	assert instance.get_min() == 'b'

	instance.minus('a')
	instance.minus('a')
	assert instance.get_max() == 'b'
