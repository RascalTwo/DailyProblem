import itertools
import sys
import collections


from typing import DefaultDict, Dict, Optional, Set



class Node:
	def __init__(self, label: str, children: Dict['Node', int] = {}):
		self.label = label
		for child in children:
			child.parent = self
		self.children = children
		self.parent: Optional['Node'] = None


def dijkstra(nodes: Set[Node], start: Node, end: Node) -> int:
	unvisited: Set[Node] = nodes.copy()
	distances: DefaultDict[Node, int] = collections.defaultdict(lambda: -sys.maxsize, { start: 0 })


	while unvisited:
		current: Node = sorted(unvisited, key = lambda node: -distances[node])[0]

		distances.update({
			neighbor: max(distances.get(neighbor, -sys.maxsize), distances[current] + distance)
			for neighbor, distance in list(current.children.items()) + (
				[(current.parent, next(distance for child, distance in current.parent.children.items() if child == current))]
				if current.parent else
				[]
			)
			if neighbor in unvisited
		})

		unvisited.remove(current)

	return distances[end]


def solve(root: Node) -> int:
	nodes: Set[Node] = set([root])

	processing = [*root.children]
	while processing:
		current = processing.pop()
		nodes.add(current)
		processing.extend(current.children)

	best = 0
	for start, end in itertools.combinations(nodes, 2):
		best = max(best, dijkstra(nodes, start, end))
	return best


def test_solve():
	assert solve(Node('a', {
		Node('b'): 3,
		Node('c'): 5,
		Node('d', {
			Node('e', {
				Node('g'): 1,
				Node('h'): 1
			}): 2,
			Node('f'): 4
		}): 8
	})) == 17
