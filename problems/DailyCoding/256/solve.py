import operator

from typing import Any, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.next == other.next


def solve(head: Node) -> Node:
	current: Node = head

	operators = [operator.le, operator.ge]
	operator_index = 0
	while current:
		operator_index = not operator_index

		first = current.next
		if not first:
			break
		second = first.next
		if not second:
			break

		if operators[operator_index](first.value, second.value):
			current = first
			continue

		first.next = second.next
		second.next = first
		current.next = second
		current = second

	return head


def test_solve():
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5)))))) == Node(1, Node(3, Node(2, Node(5, Node(4)))))
