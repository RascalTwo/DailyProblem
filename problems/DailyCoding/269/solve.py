import collections

from typing import DefaultDict, List, Set



def solve(initial_state: str) -> str:
	def append_mutation(i: int, char: str):
		target = i + (-1 if char == 'L' else 1)
		if 0 <= target < len(positions) and positions[target] == '.':
			mutating_positions[target].add(char)


	positions: List[str] = list(initial_state)

	mutating_positions: DefaultDict[int, Set[str]] = collections.defaultdict(set)
	for i, char in enumerate(positions):
		if char in 'LR':
			append_mutation(i, char)

	while mutating_positions:
		copy = mutating_positions.copy()
		mutating_positions.clear()
		for i, forces in copy.items():
			if forces == {'L', 'R'} or positions[i] != '.':
				continue
			char = next(iter(forces))
			positions[i] = char
			append_mutation(i, char)

	return ''.join(positions)


def test_solve():
	assert solve('.L.R....L.') == 'LL.RRRLLL.'
	assert solve('..R...L.L.') == '..RR.LLLL.'
