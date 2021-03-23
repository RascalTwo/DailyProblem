import heapq


from typing import List, Tuple



class Stack:
	def __init__(self):
		self.heap: List[Tuple[int, int]] = []


	def push(self, item: int):
		heapq.heappush(self.heap, (-len(self.heap), -item))


	def pop(self):
		if not self.heap:
			raise IndexError('pop from empty stack')
		return -heapq.heappop(self.heap)[1]


def test_solve():
	s = Stack()
	values = [9, 47, 3, 1, 47, 89, 6, 5, 1]
	for i in values:
		s.push(i)
	for i in reversed(values):
		assert s.pop() == i

	try:
		s.pop()
		assert False, 'did not throw exception when poping from empty stack'
	except IndexError:
		pass
