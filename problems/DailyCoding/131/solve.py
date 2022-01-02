import random

from typing import Any, Dict, List, Optional


class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next

		self.random: Node = None  # type: ignore


	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.value == other.value and self.next == other.next and self.random.value == other.random.value


def create_linked_list(length: int) -> Node:
	head = Node(0)

	nodes: List[Node] = [head]

	current = head
	for i in range(1, length + 1):
		current.next = Node(i)
		current = current.next
		nodes.append(current)

	for node in nodes:
		node.random = random.choice(nodes)

	return head

def solve(head: Node) -> Node:
	old_nodes: List[Node] = []
	nodes: List[Node] = []
	current = head
	while current:
		old_nodes.append(current)
		nodes.append(Node(current.value))
		current = current.next

	for i, node in enumerate(nodes[1:]):
		nodes[i].next = node

	for i, node in enumerate(nodes):
		node.random = nodes[old_nodes.index(old_nodes[i].random)]

	return nodes[0]


def test_solve():
	ll = create_linked_list(5)
	cloned = solve(ll)
	assert cloned == ll
	ll.value = -1
	assert cloned != ll
