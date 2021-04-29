from typing import Any, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next


	def __eq__(self, o: Any) -> bool:
		return isinstance(o, Node) and self.value == o.value and self.next == o.next


	def __len__(self):
		return 1 + (len(self.next) if self.next else 0)


def solve(root: Node, k: int) -> Node:
	prev: Optional[Node] = None
	current: Optional[Node] = root
	for _ in range(len(root) - k):
		assert current
		prev = current
		current = current.next
	assert prev
	prev.next = None

	assert current
	new_root = current
	prev = None
	while current:
		prev = current
		current = current.next
	assert prev
	prev.next = root

	return new_root


def test_solve():
	assert solve(Node(7, Node(7, Node(3, Node(5)))), 2) == Node(3, Node(5, Node(7, Node(7))))
	assert solve(Node(1, Node(2, Node(3, Node(4, Node(5))))), 3) == Node(3, Node(4, Node(5, Node(1, Node(2)))))
