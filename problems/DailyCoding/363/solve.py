from typing import Any



class Combiner:
	def __init__(self, initial: int):
		self.value = initial
		self.adding = True

	def __call__(self, value: int):
		if self.adding:
			self.value += value
		else:
			self.value -= value
		self.adding = not self.adding
		return self

	def __eq__(self, other: Any):
		return isinstance(other, (int, float)) and self.value == other


def solve(first: int):
	return Combiner(first)


def test_solve():
	assert solve(7) == 7
	assert solve(1)(2)(3) == 0
	assert solve(-5)(10)(3)(9) == 11
