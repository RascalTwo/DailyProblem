from typing import Iterable, List, Set, Tuple



def traverse_nodes(connections: List[Tuple[str, str]]) -> Set[str]:
	visited: Set[str] = {*connections.pop()}
	while True:
		for i, connection in enumerate(connections[:]):
			if any(node in visited for node in connection):
				visited |= set(connection)
				del connections[i]
				break
		else:
			break

	return visited


def solve(connections: List[Tuple[str, str]]) -> Iterable[Tuple[str, str]]:
	nodes = traverse_nodes(connections[:])
	yield from (
		connection
		for i, connection in enumerate(connections)
		if traverse_nodes(connections[:i] + connections[i + 1:]) != nodes
	)



def test_solve():
	assert list(solve([
		('A', 'B'),
		('A', 'C'),
		('A', 'D'),
		('B', 'C'),
		('C', 'D'),
		('D', 'E')
	])) == [('D', 'E')]

	assert list(solve([
		('A', 'B'),
		('B', 'C'),
		('C', 'A'),
		('X', 'Y'),
		('Y', 'Z'),
		('Z', 'X'),
		('C', 'X')
	])) == [('C', 'X')]
