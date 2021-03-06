from typing import Any, Iterator



class PeekableInterface(object):
	def __init__(self, iterator: Iterator[Any]):
		self.iterator = iterator
		self._next = next(self.iterator, None)


	def peek(self):
		if self._next is None:
			raise StopIteration
		return self._next


	def next(self):
		value = self.peek()
		self._next = next(self.iterator, None)
		return value


	def hasNext(self):
		return self._next is not None


def test_solve():
	pi = PeekableInterface(iter(range(10)))
	for i in range(10):
		assert pi.peek() == i
		assert pi.hasNext()
		assert pi.next() == i

	assert pi.hasNext() is False

	try:
		pi.peek()
		assert False, 'Did not StopIteration'
	except StopIteration:
		pass
