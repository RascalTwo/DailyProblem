import collections


from typing import Counter



class HitCounter:
	def __init__(self):
		self.hits: Counter[int] = collections.Counter()


	def record(self, timestamp: int):
		self.hits[timestamp] += 1


	def range(self, lower: int, upper: int) -> int:
		return sum(hits for when, hits in self.hits.items() if lower <= when <= upper)


	def total(self):
		return sum(self.hits.values())


def test_solve():
	hc = HitCounter()
	assert hc.total() == 0

	for timestamp in (1, 5, 10):
		hc.record(timestamp)
		hc.record(timestamp)
	assert hc.total() == 6

	assert hc.range(15, 20) == 0
	assert hc.range(1, 5) == 4
	assert hc.range(1, 10) == 6
