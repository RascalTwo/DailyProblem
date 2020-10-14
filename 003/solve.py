import json

from typing import Optional



class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def serialize(root: Optional[Node]) -> str:
	return json.dumps({'val': root.val, 'left': serialize(root.left), 'right': serialize(root.right)} if root else None)


def deserialize(string: str) -> Node:
	return Node(args['val'], deserialize(args['left']), deserialize(args['right'])) if (args := json.loads(string)) else None


def test_solve():
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	assert deserialize(serialize(node)).left.left.val == 'left.left'

