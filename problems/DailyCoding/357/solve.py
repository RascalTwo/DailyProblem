from typing import Any, Optional


class Node:
	def __init__(self, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.left = left
		self.right = right

	def __eq__(self, other: Any) -> bool:
		return isinstance(other, Node) and self.left == other.left and self.right == other.right

def solve(encoded: str) -> Optional[Node]:
	inner = encoded[1:-1]
	left = None
	right = None
	if inner[0] == '0':
		inner = inner[1:]
		left = False
	if inner[-1] == '0':
		inner = inner[:-1]
		right = False

	if not inner:
		return Node()

	if left is False:
		return Node(None, solve(inner))
	elif right is False:
		return Node(solve(inner))

	opens = 0
	i = 0
	for i, char in enumerate(inner):
		if char == '(':
			opens += 1
		elif char == ')':
			opens -= 1

		if i and not opens:
			break

	i += 1
	return Node(solve(inner[:i]), solve(inner[i:]))



def test_solve():
	assert solve('(00)') == Node()
	assert solve('((00)(00))') == Node(Node(), Node())
	assert solve('((((00)0)0)0)') == Node(Node(Node(Node())))
