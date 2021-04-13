from typing import Any, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.next == other.next


def solve(root: Node) -> Node:
	current: Optional[Node] = Node(0, root)
	while current:
		bubble: Node = current
		while bubble.next:
			if bubble.value > bubble.next.value:
				value = bubble.value
				bubble.value = bubble.next.value
				bubble.next.value = value
			bubble = bubble.next
		current = current.next
	return root



def test_solve():
	assert solve(Node(4, Node(1, Node(-3, Node(99))))) == Node(-3, Node(1, Node(4, Node(99))))
