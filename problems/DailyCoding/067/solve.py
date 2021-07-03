import collections
import heapq

from typing import Any, Hashable, List, Optional, OrderedDict, Tuple



class LFUCache:
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.entries: OrderedDict[Hashable, Any] = collections.OrderedDict()
		self.frequencies: List[Tuple[int, Hashable]] = []


	def set(self, key: Hashable, value: Any):
		if len(self.entries) == self.capacity:
			removing = heapq.heappop(self.frequencies)
			self.entries.pop(removing[1])

		self.entries[key] = value
		heapq.heappush(self.frequencies, (0, key))


	def get(self, key: Hashable) -> Optional[Any]:
		value = self.entries.get(key, None)
		if value is None:
			return None

		heapq.heappush(self.frequencies, (
			self.frequencies.pop(next(
				i
				for i, (_, finding_key) in enumerate(self.frequencies)
				if key == finding_key
			))[0] + 1,
			key
		))
		return value


	def __len__(self):
		return len(self.entries)


def test_solve():
	lfu = LFUCache(3)
	lfu.set(0, 0)
	lfu.set(1, 1)
	lfu.set(2, 2)
	assert lfu.get(0) == 0
	assert len(lfu) == 3

	lfu.set(3, 3)
	assert len(lfu) == 3
	assert lfu.get(1) is None
	assert lfu.get(0) == 0
	assert lfu.get(2) == 2

	lfu.set(4, 4)
	assert lfu.get(3) is None
