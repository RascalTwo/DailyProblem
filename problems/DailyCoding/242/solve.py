from typing import Dict



class SubscriberTracker:
	def __init__(self):
		self.changes: Dict[int, int] = {}


	def update(self, hour: int, value: int):
		if hour not in self.changes:
			self.changes[hour] = 0
		self.changes[hour] += value


	def query(self, start: int, end: int) -> int:
		change = 0
		for hour in range(start, end + 1):
			change += self.changes.get(hour, 0)
		return change


def test_solve():
	changes = [1, 5, 4, 8, 9, 6, 4, 5, 3, 2, 1, 5, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2]

	tracker = SubscriberTracker()
	for hour, change in enumerate(changes):
		tracker.update(hour, change)

	assert tracker.query(0, 23) == sum(changes)
	assert tracker.query(11, 23) == sum(changes[11:])
	assert tracker.query(0, 12) == sum(changes[:13])

