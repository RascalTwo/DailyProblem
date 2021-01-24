from typing import Any, Optional



class Stack:
	def __init__(self):
		self.values = []


	def push(self, value: Any):
		self.values.append(value)


	def pop(self) -> Optional[Any]:
		return self.values.pop() if self.values else None


	def __bool__(self):
		return bool(self.values)


class Queue:
	def __init__(self):
		self.input = Stack()
		self.output = Stack()


	def enqueue(self, element: Any):
		self.input.push(element)


	def dequeue(self) -> Optional[Any]:
		if not self.input and not self.output:
			return None

		if not self.output:
			while self.input:
				self.output.push(self.input.pop())

		return self.output.pop()



def test_solve():
	values = [1, 2, 3]

	queue = Queue()

	for value in values:
		queue.enqueue(value)

	for value in values:
		assert queue.dequeue() == value
