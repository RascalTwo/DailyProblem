from typing import Generic, List, Optional, TypeVar, Union


T = TypeVar('T')

class TwoDIterator(Generic[T]):
	def __init__(self, arrays: List[List[T]]):
		self.arrays = arrays
		self._index: Optional[complex] = 0 + 0j
		self._next_index: Optional[complex] = self._increment_index()


	def _increment_index(self):
		if self._index is None:
			return None

		index = self._index + 1j
		if index.imag >= len(self.arrays[int(index.real)]):
			while True:
				index = (index.real + 1) + 0j
				if index.real >= len(self.arrays):
					index = None
					break
				if self.arrays[int(index.real)]:
					break
		return index


	def next(self) -> T:
		if not self.has_next():
			raise StopIteration()

		assert self._index
		value = self.arrays[int(self._index.real)][int(self._index.imag)]
		self._index = self._next_index
		self._next_index = self._increment_index()
		return value


	def has_next(self):
		return self._index or self._next_index


	def __iter__(self):
		while self.has_next():
			yield self.next()


def test_solve():
	iterator = TwoDIterator([[1, 2], [3], [], [4, 5, 6]])

	values: List[int] = []
	while iterator.has_next():
		values.append(iterator.next())
	assert values == [1, 2, 3, 4, 5, 6]


	assert list(TwoDIterator([[1, 2], [3], [], [4, 5, 6]])) == [1, 2, 3, 4, 5, 6]
