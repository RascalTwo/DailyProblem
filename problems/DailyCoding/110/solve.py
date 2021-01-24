from typing import Iterable, List, Optional



class Node:
	def __init__(self, value: int, left: Optional['Node'], right: Optional['Node']):
		self.value = value
		self.left = left
		self.right = right


def solve(root: Node) -> Iterable[List[int]]:
	paths: List[List[Node]] = [[root]]
	while paths and (path := paths.pop(0)) and (last := path[-1]):
		if not last.left and not last.right:
			yield [node.value for node in path]
		else:
			paths.extend(path + [node] for node in (last.left, last.right) if node)



def test_solve():
	assert list(solve(Node(1,
		Node(2, None, None),
		Node(3,
			Node(4, None, None),
			Node(5, None, None)
		)
	))) == [[1, 2], [1, 3, 4], [1, 3, 5]]
