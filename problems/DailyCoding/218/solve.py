from typing import Dict, List



def solve(graph: Dict[str, List[str]]) -> Dict[str, List[str]]:
	new_graph: Dict[str, List[str]] = {}
	for origin, dests in graph.items():
		for dest in dests:
			new_graph.setdefault(dest, []).append(origin)
	return new_graph

def test_solve():
	assert solve({
		'A': ['B'],
		'B': ['C']
	}) == {
		'C': ['B'],
		'B': ['A']
	}

	assert solve({
		'A': ['B', 'C'],
		'B': ['A', 'D'],
	}) == {
		'A': ['B'],
		'B': ['A'],
		'C': ['A'],
		'D': ['B']
	}
