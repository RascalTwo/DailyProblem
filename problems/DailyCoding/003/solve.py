import json

from typing import Any, Optional, Generic, TypeVar



T = TypeVar('T')

class Node(Generic[T]):
	def __init__(self, val: T, left: Optional['Node[T]'] = None, right: Optional['Node[T]'] = None):
		self.val = val
		self.left = left
		self.right = right


def serialize(root: Optional[Node[Any]]) -> str:
	return json.dumps({'val': root.val, 'left': serialize(root.left), 'right': serialize(root.right)} if root else None)


def deserialize(string: str) -> Optional[Node[Any]]:
	return Node(args['val'], deserialize(args['left']), deserialize(args['right'])) if (args := json.loads(string)) else None


def test_solve():
	node = Node('root', Node('left', Node('left.left')), Node('right'))
	deserialized = deserialize(serialize(node))
	assert deserialized
	assert deserialized.left
	assert deserialized.left.left
	assert deserialized.left.left.val == 'left.left'

