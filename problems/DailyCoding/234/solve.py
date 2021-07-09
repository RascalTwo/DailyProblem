import heapq

from typing import Dict, List, Optional, Set, Tuple



def contains_cycle(edges: List[Tuple[int, str, str]], parent: Optional[str], current: str, visited: Set[str] = set()) -> bool:
	visited.add(current)

	for edge in edges:
		if current not in edge:
			continue
		other = edge[2 if current == edge[1] else 1]
		if other == parent:
			continue
		if other in visited:
			return True
		if contains_cycle(edges, current, other, visited): # type: ignore
			return True

	return False


def test_contains_cycle():
	assert contains_cycle([(0, 'A', 'B'), (0, 'B', 'C')], None, 'A', set()) is False
	assert contains_cycle([(0, 'A', 'B'), (0, 'B', 'C'), (0, 'C', 'A')], None, 'A', set()) is True
	assert contains_cycle([(0, 'A', 'B'), (0, 'B', 'C'), (0, 'D', 'A')], None, 'A', set()) is False


def solve(connections: Dict[str, Dict[str, int]]) -> List[Tuple[str, str]]:
	edges: List[Tuple[int, str, str]] = []
	for origin, destinations in connections.items():
		for dest, weight in destinations.items():
			heapq.heappush(edges, (-weight, origin, dest))

	mst: List[Tuple[int, str, str]] = []
	while edges:
		next_edge = heapq.heappop(edges)
		mst.append(next_edge)
		if contains_cycle(mst, None, next_edge[1], set()):
			mst.pop()

	return [edge[1:] for edge in mst] # type: ignore


def test_solve():
	assert solve({
		'A': {'B': 1, 'D': 4, 'E': 3},
		'B': {'A': 1, 'D': 4, 'E': 2},
		'C': {'E': 4, 'F': 5},
		'D': {'A': 4, 'B': 4, 'E': 4},
		'E': {'A': 3, 'B': 2, 'C': 4, 'D': 4, 'F': 7},
		'F': {'C': 5, 'E': 7}
	}) == [('E', 'F'), ('C', 'F'), ('A', 'D'), ('B', 'D'), ('D', 'E')]

	assert solve({
		'A': {'B': 100, 'D': 4, 'E': 3},
		'B': {'A': 100, 'D': 4, 'E': 2},
		'C': {'E': 4, 'F': 5},
		'D': {'A': 4, 'B': 4, 'E': 4},
		'E': {'A': 3, 'B': 2, 'C': 4, 'D': 4, 'F': 7},
		'F': {'C': 5, 'E': 7}
	}) == [('A', 'B'), ('E', 'F'), ('C', 'F'), ('A', 'D'), ('D', 'E')]
