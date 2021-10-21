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
		('facebok', 1), ('facebok', 3), ('facebok', 5),
		('rreddit', 2), ('rreddit', 6),
		('twitter', 1), ('twitter', 2), ('twitter', 3), ('twitter', 4), ('twitter', 5),
		('example', 4), ('example', 5), ('example', 6), ('example', 7),
		('myspace', 1), ('myspace', 3), ('myspace', 5), ('myspace', 6)
	) == [('facebok', 'myspace')]
	assert solve(2,
		('facebok', 1), ('facebok', 3), ('facebok', 5),
		('rreddit', 2), ('rreddit', 6),
		('twitter', 1), ('twitter', 2), ('twitter', 3), ('twitter', 4), ('twitter', 5),
		('example', 4), ('example', 5), ('example', 6), ('example', 7),
		('myspace', 1), ('myspace', 3), ('myspace', 5), ('myspace', 6)
	) == [('facebok', 'myspace'), ('facebok', 'twitter')]
