from typing import Any, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.next == other.next


	def __str__(self):
		return f'v={self.value} n=({self.next})'


	def __repr__(self):
		return str(self)


def solve(root: Node) -> Node:
	if not root.next:
		return root

	head: Node = root
	start: Node = head
	while start and start.next:
		end = start
		total = start.value
		while end:
			end = end.next  # type: ignore
			if not end:
				continue

			total += end.value
			if total == 0:
				break

		if total != 0:
			if start != root:
				head = head.next  # type: ignore
			start = start.next
			continue

		if start == root:
			root = end.next  # type: ignore
			start = root
			head = root
		else:
			head.next = end.next  # type: ignore
			start = head


	return root


def test_solve():
	assert solve(Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6))))))) == Node(5)
	assert solve(Node(5, Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6)))))))) == Node(5, Node(5))
	assert solve(Node(-5, Node(3, Node(4, Node(-7, Node(5, Node(-6, Node(6)))))))) == None
