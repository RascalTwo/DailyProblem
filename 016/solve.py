class OrderRecorder:
	def __init__(self, max_orders: int):
		self.max_orders = max_orders
		self.last = 1
		self.orders = {}


	def record(self, order_id: int) -> None:
		if self.last > self.max_orders:
			del self.orders[self.last - self.max_orders]

		self.last += 1
		self.orders[self.last] = order_id


	def get_last(self, i: int) -> int:
		return self.orders[self.last - i + 1]


def test_solve():
	db = OrderRecorder(3)
	order_ids = [111, 222, 333, 444]
	for order_id in order_ids[:3]:
		db.record(order_id)
	for i, order_id in enumerate(reversed(order_ids[:3])):
		assert db.get_last(i + 1) == order_id

	db.record(order_ids[3])
	for i, order_id in enumerate(reversed(order_ids[1:4])):
		assert db.get_last(i + 1) == order_id

	try:
		db.get_last(4)
		assert False, 'Expected IndexError'
	except IndexError:
		pass
