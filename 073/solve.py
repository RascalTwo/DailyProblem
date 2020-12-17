
from typing import Optional



class Node:
	def __init__(self, value: int, next: Optional['Node']):
		self.value = value
		self.next = next


	def __iter__(self):
		current = self
		while current:
			yield current.value
			current = current.next


def solve(head: Node) -> Node:
	prev = None
	current = head
	while current:
		nxt = current.next
		current.next = prev
		prev = current
		current = nxt

	assert prev
	return prev


def test_solve():
	forwards = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
	assert list(forwards) == [1, 2, 3, 4, 5]
	assert list(solve(forwards)) == [5, 4, 3, 2, 1]
