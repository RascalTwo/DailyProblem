from typing import Any, Dict, Generic, Optional, TypeVar



T = TypeVar('T')


class Node(Generic[T]):
	def __init__(self, value: T, next_prev: int):
		self.value = value
		self.next_prev = next_prev


class XORLinkedList(Generic[T]):
	def __init__(self):
		self.head: Optional[Node[T]] = None


	def add(self, element: T):
		node = dereference_pointer(Node(element, 0))

		if not self.head:
			self.head = node
			return

		prev = None
		current = self.head
		while True:
			next_node = get_pointer(id(prev) ^ current.next_prev)
			if next_node:
				prev, current = current, next_node
				continue

			current.next_prev = id(prev) ^ id(node)
			node.next_prev = id(current) ^ id(None)
			return


	def get(self, index: int) -> Optional[Node[T]]:
		if not self.head:
			return None

		prev = None
		current = self.head
		for _ in range(index):
			next_node = get_pointer(id(prev) ^ current.next_prev)
			if not next_node:
				return None
			prev, current = current, next_node

		return current


POINTERS: Dict[int, Node[Any]] = {}
def get_pointer(pointer: int) -> Optional[Node[Any]]:
	return POINTERS.get(pointer, None)
def dereference_pointer(node: Node[T]) -> Node[T]:
	POINTERS[id(node)] = node
	return node


def test_solve():
	VALUES = ('first', 'second', 'third')

	ll = XORLinkedList[str]()
	for value in VALUES:
		ll.add(value)

	for i, char in enumerate(VALUES):
		node = ll.get(i)
		assert node is not None
		assert node.value == char
