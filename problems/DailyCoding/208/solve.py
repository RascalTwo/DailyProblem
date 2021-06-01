from typing import Any, List, Optional, Tuple



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next

	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.next == other.next

	def __iter__(self):
		current = self
		while current:
			yield current.value
			current = current.next


def solve(head: Node, k: int) -> Node:
	tail = head

	current = head
	while current:
		next = current.next

		if current.value < k:
			current.next = head
			head = current
		else:
			tail.next = current
			tail = current

		current = next

	tail.next = None

	return head


def test_solve():
	def assert_correct(head: Node, k: int):
		result = solve(head, k)

		split: List[List[Tuple[int, int]]] = [[], []]
		for i, value in enumerate(result):
			split[value >= k].append((i, value))

		for i, value in split[0]:
			for oi, other in split[1]:
				assert i < oi
				assert value < other

	assert_correct(Node(5, Node(1, Node(8, Node(0, Node(3))))), 3)
	assert_correct(Node(7, Node(5, Node(3, Node(1)))), 4)
