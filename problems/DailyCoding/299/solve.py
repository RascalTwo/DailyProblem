import itertools
import copy

from typing import Dict, List, Set, Tuple

Connections = Dict[str, Dict[str, int]]



def collect_nodes(connections: Connections, start: str) -> Tuple[Set[str], int]:
	visited: Set[str] = set()
	cost = 0
	unvisited = [start]
	while unvisited:
		node = unvisited.pop()
		visited.add(node)
		unvisited += list(connections.get(node, {}).keys())
		cost += sum(connections.get(node, {}).values())

	return visited, cost



def solve(connections: Connections, start: str) -> Tuple[Connections, int]:
	all_nodes, worst_cost = collect_nodes(connections, start)

	edges: List[Tuple[str, str]] = []
	for origin, destinations in connections.items():
		for destination in destinations:
			edges.append((origin, destination))

	best = (connections, worst_cost)

	for count in range(1, len(edges) - (len(connections) - 1) + 1):
		for removing in itertools.permutations(edges, count):
			attempt = copy.deepcopy(connections)
			for edge in removing:
				del attempt[edge[0]][edge[1]]

			found, cost = collect_nodes(attempt, start)
			if all_nodes == found and cost < best[1]:
				best = attempt, cost


	return best


def test_solve():
	assert solve({
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
	}, 'plant') == ({
    'plant': {'A': 1, 'B': 5},
    'A': {},
    'B': {'C': 10},
    'C': {}
	}, 16)
