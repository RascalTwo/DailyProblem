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


def solve_linked_list(*nodes: Optional[Node]) -> Node:
	total = 0
	place = 1
	while any(nodes):
		total += sum(node.value * place for node in nodes if node)
		nodes = [node.next if node else None for node in nodes]  # type: ignore
		place *= 10

	digits = [int(digit) for digit in str(total)][::-1]
	root = Node(digits[0])
	current = root
	for digit in digits[1:]:
		current.next = Node(digit)
		current = current.next
	return root


def test_solve():
	big = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	assert solve_numeric(big, big) == 54321 + 54321
	assert solve_numeric(big) == 54321
	assert solve_numeric(big, big, big) == 54321 + 54321 + 54321

	assert solve_numeric(Node(9, Node(9)), Node(5, Node(2))) == 99 + 25
	assert solve_numeric(Node(9, Node(9)), Node(5, Node(2)), Node(1)) == 99 + 25 + 1

	assert solve_linked_list(big, big) == Node(2, Node(4, Node(6, Node(8, Node(0, Node(1))))))
	assert solve_linked_list(Node(9, Node(9)), Node(5, Node(2))) == Node(4, Node(2, Node(1)))
