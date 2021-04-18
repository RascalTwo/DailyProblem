from typing import Any, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.next == other.next


def reverse(first: Node) -> Node:
	prev = None
	current = first
	while current:
		nxt = current.next
		current.next = prev
		prev = current
		current = nxt

	assert prev
	return prev


def solve(root: Node):
	prev = root
	current: Optional[Node] = root.next
	while current:
		rev = reverse(current)
		prev.next = rev
		current = rev.next
		prev = prev.next

	return root

def test_solve():
	assert solve(Node(1, Node(2, Node(3, Node(4))))) == Node(1, Node(4, Node(2, Node(3))))
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5)))))) == Node(1, Node(5, Node(2, Node(4, Node(3)))))
