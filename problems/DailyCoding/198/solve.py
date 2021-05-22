import collections


from typing import DefaultDict, List, Set, Tuple



def solve(integers: List[int]) -> List[int]:
	divisibles: DefaultDict[int, Set[int]] = collections.defaultdict(set)
	for i, first in enumerate(integers):
		for j, second in enumerate(integers):
			if i == j:
				continue
			if first % second == 0 or second % first == 0:
				divisibles[i].add(j)

	remaining: List[Tuple[int, Set[int]]] = list(divisibles.items())
	while True:
		lengths = set(len(lst) for _, lst in remaining)
		if len(lengths) == 1:
			return list(integers[i] for i, _ in remaining)

		remaining = sorted(remaining, key=lambda pair: len(pair[1]), reverse=True)
		removing = remaining.pop()[0]
		for _, lst in remaining:
			lst.discard(removing)


def test_solve():
	assert solve([3, 5, 10, 20, 21]) == [5, 10, 20]
	assert solve([1, 3, 6, 24]) == [1, 3, 6, 24]
	assert solve([1, 3, 6, 24, 12, 4, 9, 18]) == [1, 3, 6, 24, 12]
