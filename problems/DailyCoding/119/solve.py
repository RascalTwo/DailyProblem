import collections


from typing import Counter, Set, Tuple



def solve(*intervals: Tuple[int, int]) -> Set[int]:
	hits: Counter[int] = collections.Counter()
	ranges = {range(start, end+1) for start, end in intervals}
	for irange in ranges:
		for i in irange:
			hits[i] += 1

	results = set()
	while hits:
		number = sorted(list(hits.items()), key = lambda pair: pair[1], reverse=True)[0][0]
		results.add(number)

		for irange in ranges:
			if number not in irange:
				continue
			for i in irange:
				if hits[i]:
					hits[i] -= 1

		for key, value in list(hits.items()):
			if not value:
				del hits[key]

	return results


def test_solve():
	assert solve((0, 3), (2, 6), (3, 4), (6, 9)) == {3, 6}
