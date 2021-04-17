import collections

from typing import Counter, List, Literal, Tuple, TypedDict, Union



DataEntry = TypedDict('DataEntry', { 'timestamp': int, 'count': int, 'type': Union[Literal['enter'], Literal['exit']]})

def solve(entries: List[DataEntry]) -> Tuple[int, int]:
	entries.sort(key = lambda entry: entry['timestamp'])

	counts: Counter[int] = collections.Counter()
	last = None
	for entry in entries:
		occupants = (last or 0) + (entry['count'] * (1 if entry['type'] == 'enter' else -1))
		counts[entry['timestamp']] = occupants
		last = occupants


	add_trailing = False
	most: Tuple[List[int], int] = ([], 0)
	for when, count in counts.items():
		if count >= most[1]:
			most = (
				[*(most[0] if count == most[1] else []), when],
				count
			)
			add_trailing = True
		elif add_trailing:
			most[0].append(when)
			add_trailing = False

	return most[0].pop(0), most[0].pop()


def test_solve():
	assert solve([
		{'timestamp': 10, 'count': 3, 'type': 'enter'},
		{'timestamp': 70, 'count': 2, 'type': 'exit'},
		{'timestamp': 20, 'count': 6, 'type': 'enter'},
		{'timestamp': 30, 'count': 1, 'type': 'enter'},
		{'timestamp': 40, 'count': 0, 'type': 'enter'},
		{'timestamp': 50, 'count': 5, 'type': 'exit'},
		{'timestamp': 60, 'count': 3, 'type': 'exit'},
	]) == (30, 50)
