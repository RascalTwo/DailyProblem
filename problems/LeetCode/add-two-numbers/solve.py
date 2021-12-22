from typing import Any, Optional



class Node:
	def __init__(self, value: int, next: Optional['Node'] = None):
		self.value = value
		self.next = next


	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, Node):
			return False

		return self.value == other.value and self.next == other.next


def solve_numeric(*nodes: Optional[Node], place: int = 1) -> int:
	if not any(nodes):
		return 0
	return (
		sum(node.value * place for node in nodes if node) +
		solve_numeric(*[node.next for node in nodes if node], place=place * 10)
	)


def solve_linked_list_one(*nodes: Optional[Node]) -> Node:
	total = 0
	place = 1
	while any(nodes):
		total += sum(node.value * place for node in nodes if node)
		nodes = [node.next for node in nodes if node]  # type: ignore
		place *= 10

	digits = [int(digit) for digit in str(total)][::-1]
	root = Node(digits[0])
	current = root
	for digit in digits[1:]:
		current.next = Node(digit)
		current = current.next
	return root


def solve_linked_list_two(*nodes: Node) -> Node:
	root = Node(0)
	current = root

	overflow: int = 0
	while any(nodes) or overflow:
		result = str(sum(node.value for node in nodes if node) + overflow)[::-1]
		overflow = int(result[1:]) if result[1:] else 0

		current.next = Node(int(result[0]))
		current = current.next

		nodes = [node.next for node in nodes if node]  # type: ignore


	assert root.next
	return root.next


def test_solve():
	big = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	assert solve_numeric(big, big) == 54321 + 54321
	assert solve_numeric(big) == 54321
	assert solve_numeric(big, big, big) == 54321 + 54321 + 54321

	assert solve_numeric(Node(9, Node(9)), Node(5, Node(2))) == 99 + 25
	assert solve_numeric(Node(9, Node(9)), Node(5, Node(2)), Node(1)) == 99 + 25 + 1

	for solve_linked_list in (solve_linked_list_one, solve_linked_list_two):
		assert solve_linked_list(big, big) == Node(2, Node(4, Node(6, Node(8, Node(0, Node(1))))))
		assert solve_linked_list(Node(9, Node(9)), Node(5, Node(2))) == Node(4, Node(2, Node(1)))

		assert solve_linked_list(Node(2, Node(4, Node(3))), Node(5, Node(6, Node(4)))) == Node(7, Node(0, Node(8)))
		assert solve_linked_list(Node(0), Node(0)) == Node(0)
		assert solve_linked_list(Node(9, Node(9, Node(9, Node(9, Node(9, Node(9, Node(9))))))), Node(9, Node(9, Node(9, Node(9))))) == Node(8, Node(9, Node(9, Node(9, Node(0, Node(0, Node(0, Node(1))))))))
