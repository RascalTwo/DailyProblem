import collections
from typing import DefaultDict, Dict, List, Set, Tuple


def solve(k: int, *individual_visits: Tuple[str, int]) -> List[Tuple[str, str]]:
	visitors: DefaultDict[str, Set[int]] = collections.defaultdict(set)
	for website, user in individual_visits:
		visitors[website].add(user)

	scores: Dict[Tuple[str, str], int] = {}
	for first in visitors.keys():
		for second in visitors.keys():
			if first == second:
				continue
			if (second, first) in scores:
				continue
			key = (first, second)
			first_users = visitors[first]
			second_users = visitors[second]
			score = len(first_users & second_users)
			score -= len(first_users.symmetric_difference(second_users))
			scores[key] = score
	return [pair for pair, _ in sorted(scores.items(), key = lambda pair: pair[1], reverse=True)[:k]]


def test_solve():
	assert solve(1,
		('a', 1), ('a', 3), ('a', 5),
		('b', 2), ('b', 6),
		('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
		('d', 4), ('d', 5), ('d', 6), ('d', 7),
		('e', 1), ('e', 3), ('e', 5), ('e', 6)
	) == [('a', 'e')]
	assert solve(2,
		('a', 1), ('a', 3), ('a', 5),
		('b', 2), ('b', 6),
		('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
		('d', 4), ('d', 5), ('d', 6), ('d', 7),
		('e', 1), ('e', 3), ('e', 5), ('e', 6)
	) == [('a', 'e'), ('a', 'c')]
