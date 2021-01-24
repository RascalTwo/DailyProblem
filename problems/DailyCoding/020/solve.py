
from typing import Any, Generic, Optional, TypeVar



T = TypeVar('T')

class Node(Generic[T]):
	def __init__(self, value: T, next: Optional['Node[T]']):
		self.value = value
		self.next = next


def reverse(first: Node[Any]) -> Node[Any]:
	prev = None
	current = first
	while current:
		nxt = current.next
		current.next = prev
		prev = current
		current = nxt

	assert prev
	return prev


def solve(alpha: Node[T], bravo: Node[T]) -> int:
	aa, bb = reverse(alpha), reverse(bravo)
	matching_value = aa.value
	while aa and bb and aa.value == bb.value:
		matching_value = aa.value
		aa, bb = aa.next, bb.next

	return matching_value


def test_solve():
	assert solve(Node(3, Node(7, Node(8, Node(10, None)))), Node(99, Node(1, Node(8, Node(10, None))))) == 8
