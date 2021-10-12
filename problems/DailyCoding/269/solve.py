import collections

from typing import DefaultDict, List, Set



def solve_iter(initial_state: str) -> str:
	def append_mutation(i: int, char: str):
		target = i + (-1 if char == '\\' else 1)
		if 0 <= target < len(positions) and positions[target] == '|':
			mutating_positions[target].add(char)


	positions: List[str] = list(initial_state)

	mutating_positions: DefaultDict[int, Set[str]] = collections.defaultdict(set)
	for i, char in enumerate(positions):
		if char in r'\/':
			append_mutation(i, char)

	while mutating_positions:
		copy = mutating_positions.copy()
		mutating_positions.clear()
		for i, forces in copy.items():
			if forces == {'\\', '/'} or positions[i] != '|':
				continue
			char = next(iter(forces))
			positions[i] = char
			append_mutation(i, char)

	return ''.join(positions)

def solve_recur(dominos: str) -> str:
	mutating: DefaultDict[int, Set[str]] = collections.defaultdict(set)

	for i, char in enumerate(dominos):
		if char == '|':
			continue
		if char == '\\' and (i == 0 or dominos[i - 1] != '|'):
			continue
		if char == '/' and (i > len(dominos) - 1 or dominos[i + 1] != '|'):
			continue
		j = i + (-1 if char == '\\' else 1)
		mutating[j].add(char)

	changing_dominos = list(dominos)
	for i, forces in mutating.items():
		if len(forces) == 2:
			continue
		changing_dominos[i] = next(iter(forces))

	new_dominos = ''.join(changing_dominos)
	if new_dominos == dominos:
		return dominos
	return solve_recur(new_dominos)


def test_solve():
	for solve in (solve_iter, solve_recur):
		assert solve(r'|\||||||\|') == r'\\||||\\\|'
		assert solve(r'||||||\|\|') == r'|||||\\\\|'
