from typing import List



class Stack:
	def __init__(self):
		self.list: List[List[int]] = []


	def pop(self, stack_number: int) -> int:
		if stack_number >= len(self.list):
			raise IndexError()
		return self.list[stack_number].pop()


	def push(self, item: int, stack_number: int):
		while stack_number >= len(self.list):
			self.list.append([])
		self.list[stack_number].append(item)


def test_solve():
	triple = Stack()
	for i in range(16):
		triple.push(i, i // 4)

	for i in range(4):
		assert [triple.pop(i) for _ in range(4)] == list(range(((i+1)*4)-1, (i*4)-1, -1))
