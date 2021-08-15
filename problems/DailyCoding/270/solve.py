import heapq

from typing import List, Optional, Set, Tuple


def contains_cycle(edges: List[Tuple[int, int, int]], parent: Optional[int], current: int, visited: Set[int] = set()) -> bool:
	visited.add(current)

	for edge in edges:
		if current not in edge[1:]:
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
	assert contains_cycle([(0, 10, 15), (0, 15, 20)], None, 10, set()) is False
	assert contains_cycle([(0, 10, 15), (0, 15, 20), (0, 20, 10)], None, 10, set()) is True
	assert contains_cycle([(0, 10, 15), (0, 15, 20), (0, 25, 10)], None, 10, set()) is False


def solve(raw_edges: List[Tuple[int, int, int]]) -> int:
	starts: List[Tuple[int, int]] = []

	edges: List[Tuple[int, int, int]] = []
	for origin, dest, weight in raw_edges:
		heapq.heappush(edges, (weight, origin, dest))
		if origin == 0:
			heapq.heappush(starts, (weight, dest))


	weight, dest = heapq.heappop(starts)
	mst: List[Tuple[int, int, int]] = [(weight, 0, dest)]

	while edges:
		next_edge = heapq.heappop(edges)
		if next_edge[1] != mst[-1][2]:
			continue
		mst.append(next_edge)
		if contains_cycle(mst, None, next_edge[1], set()):
			mst.pop()

	return sum(edge[0] for edge in mst)


def test_solve():
	assert solve([
		(0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
	]) == 9
