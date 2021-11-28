import sys

from typing import Dict



class PriceTracker:
	def __init__(self):
		self.prices: Dict[int, float] = {}

	@property
	def min(self):
		return min(self.prices.values()) if self.prices else float(-sys.maxsize)

	@property
	def max(self):
		return max(self.prices.values()) if self.prices else float(sys.maxsize)

	@property
	def average(self):
		return sum(self.prices.values()) / len(self.prices) if self.prices else 0

	def add(self, timestamp: int, price: float):
		self.prices[timestamp] = price

	def update(self, timestamp: int, price: float):
		self.add(timestamp, price)

	def remove(self, timestamp: int):
		if timestamp in self.prices:
			del self.prices[timestamp]


def test_solve():
	tracker = PriceTracker()

	def assert_min_max_average(min: float, max: float, average: float):
		assert tracker.min == min
		assert tracker.max == max
		assert tracker.average == average

	assert_min_max_average(float(-sys.maxsize), float(sys.maxsize), 0)
	tracker.add(0, 0)
	assert_min_max_average(0, 0, 0)
	tracker.add(1, 1)
	assert_min_max_average(0, 1, 0.5)
	tracker.add(2, 2)
	assert_min_max_average(0, 2, 1)
	tracker.add(3, -1)
	assert_min_max_average(-1, 2, 0.5)
	tracker.add(4, 5)
	assert_min_max_average(-1, 5, 1.4)
	tracker.remove(3)
	assert_min_max_average(0, 5, 2)
	tracker.update(4, 4)
	assert_min_max_average(0, 4, 1.75)
