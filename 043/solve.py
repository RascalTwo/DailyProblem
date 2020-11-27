from typing import List, Optional



class Stack:
	def __init__(self) -> None:
		self.values: List[int] = []
		self.most: Optional[int] = None


	def push(self, val: int):
		empty = self.most is None
		greater = not empty and val > self.most
		self.values.append(val if not greater else (2 * val) - self.most)
		if empty or greater:
			self.most = val


	def pop(self) -> Optional[int]:
		if self.most is None:
			return None

		removing = self.values.pop()
		if removing < self.most:
			return removing

		returning = self.most
		self.most = (2 * self.most) - removing if self.values else None
		return returning


	def max(self) -> Optional[int]:
		return self.most



def test_solve():
	S = Stack()
	for value, max in [(1, 1), (5, 5), (3, 5), (10, 10)]:
		S.push(value)
		assert S.max() == max

	for value, max in [(10, 5), (3, 5), (5, 1), (1, None)]:
		assert S.pop() == value
		assert S.max() == max
