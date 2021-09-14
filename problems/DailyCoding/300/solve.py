import io
import collections

from typing import DefaultDict, Iterable, Set, Tuple, Union



def solve(stream: io.TextIOWrapper) -> Iterable[Union[str, Tuple[int, int, int]]]:
	voted: Set[int] = set()

	votes: DefaultDict[int, int] = collections.defaultdict(int)

	for line in (line.strip() for line in stream.readlines()):
		if not line:
			continue

		vid, cid = map(int, (id.strip() for id in line[1:-1].split(',')))
		if vid in voted:
			yield f'Fraud: {line}'
			continue

		voted.add(vid)
		votes[cid] += 1
		yield tuple(cid for cid, _ in sorted(votes.items(), key = lambda item: item[1], reverse=True)[0:3])  # type: ignore


def test_solve():
	assert list(solve(io.StringIO('''
(0, 10)
(1, 11)
(2, 10)
(3, 10)
(4, 12)
(5, 10)
(6, 9)
(7, 9)
(8, 9)
(9, 9)
(9, 9)
(10, 9)
'''.strip()))) == [(10,), (10, 11), (10, 11), (10, 11), (10, 11, 12), (10, 11, 12), (10, 11, 12), (10, 9, 11), (10, 9, 11), (10, 9, 11), 'Fraud: (9, 9)', (9, 10, 11)]
