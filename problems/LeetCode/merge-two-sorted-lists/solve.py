from typing import Optional, Tuple, Union



class Node:
	def __init__(self, value: Union[int, float], next: Optional['Node']):
		self.value = value
		self.next = next

	def __iter__(self):
		current = self
		while current:
			yield current.value
			current = current.next


def solve(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
	if not list1 or not list2:
		return list1 or list2

	head = Node(float('-inf'), Node(float('-inf'), None))
	tail = head.next
	assert tail


	while list1 and list2:
		least: Tuple[int, Node] = (0, list1)
		if list2.value <= least[1].value:
			least = (1, list2)

		head_index, list_head = least
		if list_head.next:
			if head_index == 0:
				list1 = list1.next
			else:
				list2 = list2.next
		else:
			if head_index == 0:
				list1 = None
			else:
				list2 = None

		tail.next = list_head
		tail = tail.next


	tail.next = list1 or list2
	assert head.next and head.next.next
	return head.next.next




def test_solve():
	assert list(iter(solve(Node(1, Node(2, Node(3, None))), Node(-1, Node(0, Node(1, Node(2, None))))))) == [-1, 0, 1, 1, 2, 2, 3]
