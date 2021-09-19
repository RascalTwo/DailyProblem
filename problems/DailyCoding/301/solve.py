import math
import hashlib
from typing import Any, Iterable, List, Literal, Union



Bit = Union[Literal[1], Literal[0]]


class BloomFilter:
	def __init__(self, count: int, error_rate: float):
		self.count = count
		self.size = int((-count * math.log(error_rate)) / math.pow(math.log(2), 2))
		self.hash_count = int((self.size / count) * math.log(2))
		self.bits: List[Bit] = [0] * self.size


	def _get_hash_bits(self, value: Any) -> Iterable[int]:
		for i in range(self.hash_count):
			yield int(hashlib.md5(f'{value}{i}'.encode()).hexdigest(), 16) % self.size


	def add(self, value: Any):
		for bit in self._get_hash_bits(value):
			self.bits[bit] = 1


	def has(self, value: Any) -> bool:
		for bit in self._get_hash_bits(value):
			if not self.bits[bit]:
				return False
		return True


def test_solve():
	values = ['abc', 'def', 'ghi', 'jkl', 'mno', 'qqq', 'zzz', 'rrr', 'aaa', 'bbb']
	filter = BloomFilter(10, 0.05)
	for value in values:
		assert not filter.has(value)
		filter.add(value)
		assert filter.has(value)
