from typing import Any, Optional, Set



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value


def has_cycle_destroy(start: Node) -> bool:
	temp = 'temp'

	node = start
	while node:
		if node.next == temp:
			return True
		nxt = node.next
		node.next = temp  # type: ignore
		node = nxt
	return False



def has_cycle_hash(start: Node) -> bool:
	seen: Set[int] = set()
	node = start
	while node:
		nid = id(node)
		if nid in seen:
			return True
		seen.add(nid)
		node = node.next
	return False


def has_cycle_floyd(start: Node) -> bool:
	slow = start
	fast = start
	while slow and fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			return True
	return False


def test_solve():
	for solve in (has_cycle_floyd, has_cycle_hash, has_cycle_destroy):
		head = Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, None)))))))
		head.next.next.next.next.next.next.next = head  # type: ignore

		assert solve(Node(1, Node(2, head))) is True
		assert solve(Node(1, Node(2, Node(3)))) is False