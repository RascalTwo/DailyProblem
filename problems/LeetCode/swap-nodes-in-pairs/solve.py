from typing import Any, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node']):
		self.value = value
		self.next = next


	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Node):
			return False

		return self.value == other.value and self.next == other.next


def solve(head: Node):
	current = head

	while current and current.next:
		temp = current.value
		current.value = current.next.value
		current.next.value = temp

		current = current.next.next

	return head



def test_solve():
	assert solve(Node(1, Node(2, Node(3, Node(4, None))))) == Node(2, Node(1, Node(4, Node(3, None))))
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5, None)))))) == Node(2, Node(1, Node(4, Node(3, Node(5, None)))))
