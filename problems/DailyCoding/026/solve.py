from typing import Any, Generic, Optional, TypeVar



T = TypeVar('T')


class Node(Generic[T]):
	def __init__(self, value: T, next: Optional['Node[T]'] = None):
		self.value = value
		self.next = next


def delete_from_end(root: Node[Any], k: int) -> Node[Any]:
	first = root
	second = root
	for _ in range(k + 1):
		if not second.next:
			return first.next if first.next else first
		second = second.next


	while second.next:
		second = second.next

		assert first.next
		first = first.next

	assert first.next
	first.next = first.next.next

	return root


def test_solve():
	for k, expected in [
		(0, (1, 2, 3)),
		(1, (1, 2, 4)),
		(2, (1, 3, 4)),
		(3, (2, 3, 4))
	]:
		root = delete_from_end(Node(1, Node(2, Node(3, Node(4, None)))), k)
		assert root.next
		assert root.next.next
		assert (root.value, root.next.value, root.next.next.value) == expected
