import collections


from typing import Any, Hashable, Optional, OrderedDict



class LRUCache:
	def __init__(self, capacity: int):
		self.capacity = capacity
		self.entries: OrderedDict[Hashable, Any] = collections.OrderedDict()


	def set(self, key: Hashable, value: Any):
		if len(self.entries) == self.capacity:
			self.entries.popitem(False)
		self.entries[key] = value


	def get(self, key: Hashable) -> Optional[Any]:
		return self.entries.get(key, None)


	def __len__(self):
		return len(self.entries)


def test_solve():
	lru = LRUCache(3)
	lru.set('a', 'b')
	lru.set(1, 2)
	lru.set('c', 'd')
	assert lru.get('a') == 'b'
	assert len(lru) == 3
	lru.set('e', 'f')
	assert len(lru) == 3
	assert lru.get('a') is None
	assert lru.get('e') == 'f'
