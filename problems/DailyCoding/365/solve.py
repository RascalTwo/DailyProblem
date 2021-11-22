from typing import List



class Quack:
	def __init__(self):
		self.values: List[int] = []

	def push(self, value: int):
		self.values.append(value)

	def pop(self):
		return self.values.pop()

	def pull(self):
		return self.values.pop(0)

	def __len__(self):
		return len(self.values)


def test_solve():
	quack = Quack()
	for _ in range(5):
		quack.push(_)
	assert len(quack) == 5
	assert quack.pop() == 4
	assert quack.pull() == 0
	assert quack.pop() == 3
	assert quack.pull() == 1
	assert quack.pop() == 2
	assert len(quack) == 0
