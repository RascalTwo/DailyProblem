from typing import List, Optional, Tuple, Union



class Node:
	def __init__(self, value: Union[int, float], next: Optional['Node']):
		self.value = value
		self.next = next

	def __iter__(self):
		current = self
		while current:
			yield current.value
			current = current.next


def solve(lists: List[Node]) -> Node:
	head = Node(float('-inf'), Node(float('-inf'), None))
	tail = head.next
	assert tail


	while lists:
		least: Tuple[int, Node] = (0, lists[0])
		for i, list_head in enumerate(lists[1:], 1):
			if list_head.value <= least[1].value:
				least = (i, list_head)

		head_index, list_head = least
		if list_head.next:
			lists[head_index] = list_head.next
		else:
			del lists[head_index]

		tail.next = list_head
		tail = tail.next


	tail.next = None
	assert head.next and head.next.next
	return head.next.next




def test_solve():
	a = Node(1, Node(2, Node(3, None)))
	b = Node(-1, Node(0, Node(1, Node(2, None))))
	c = Node(2, Node(3, Node(4, Node(5, None))))
	assert list(iter(solve([a, b, c]))) == [-1, 0, 1, 1, 2, 2, 2, 3, 3, 4, 5]
