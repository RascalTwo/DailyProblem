
from typing import Any, Optional, Tuple



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next

	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.next == other.next

	def __len__(self):
		return 1 + (len(self.next) if self.next else 0)


def reverse(head: Node, k: int) -> Tuple[Node, Optional[Node]]:
	prev = None
	current = head
	nxt = None
	i = 0
	while current and i != k:
		nxt = current.next
		current.next = prev
		prev = current
		current = nxt
		i += 1

	assert prev
	return prev, nxt


def solve(head: Node, k: int):
	if k == 1:
		return head

	first = True
	current = head
	reversed_tail: Optional[Node] = None
	while current and len(current) >= k:
		current, remaining = reverse(current, k)
		if first:
			head = current
			first = not first
		else:
			assert reversed_tail
			reversed_tail.next = current

		while current.next:
			current = current.next
		current.next = remaining
		reversed_tail = current
		current = current.next

	return head


def test_solve():
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5))))), 1) == Node(1, Node(2, Node(3, Node(4, Node(5)))))
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5))))), 2) == Node(2, Node(1, Node(4, Node(3, Node(5)))))
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5))))), 3) == Node(3, Node(2, Node(1, Node(4, Node(5)))))
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5))))), 4) == Node(4, Node(3, Node(2, Node(1, Node(5)))))
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5))))), 5) == Node(5, Node(4, Node(3, Node(2, Node(1)))))
