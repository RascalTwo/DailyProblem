from typing import List, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node']):
		self.value = value
		self.next = next


def solve(root: Node) -> bool:
	values: List[int] = []
	current = root
	while current:
		values.append(current.value)
		current = current.next

	current = root
	while current:
		if values.pop() != current.value:
			return False
		current = current.next

	return True


def test_solve():
	assert solve(Node(1, Node(4, Node(3, Node(4, Node(1, None)))))) is True
	assert solve(Node(1, Node(4, Node(3, Node(5, Node(1, None)))))) is False
