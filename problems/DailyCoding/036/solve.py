from typing import Optional, Tuple



class Node:
	def __init__(self, value: int, left: Optional['Node'] = None, right: Optional['Node'] = None):
		self.value = value
		self.left = left
		self.right = right


def recur(root: Optional[Node]) -> Tuple[int, int]:
	return (
		(0, 0)
		if not root else
		tuple(sorted({root.value} | set(recur(root.left)) | set(recur(root.right)))[::-1][:2])
	)  # type: ignore


def solve(root: Node) -> int:
	return recur(root)[1]


def test_solve():
	assert solve(Node(0,
		Node(2,
			Node(1),
			Node(3),
		),
		Node(5,
			Node(4),
			Node(7,
				Node(6),
				Node(8)
			)
		)
	)) == 7
