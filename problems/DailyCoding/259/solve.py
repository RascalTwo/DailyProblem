import collections

from typing import DefaultDict, List, Tuple



def solve(words: List[str]) -> str:
	best_ratio: Tuple[str, float] = (words[0], 0)

	# ['key': [even count, total count]]
	starts: DefaultDict[str, List[int]] = collections.defaultdict(lambda: [0, 0])
	for word in words:
		letter = word[0]
		counts = starts[letter]
		counts[0] += len(word) % 2 == 0
		counts[1] += 1
		if (ratio := counts[0] / counts[1]) > best_ratio[1]:
			best_ratio = letter, ratio

	return best_ratio[0]



def test_solve():
	assert solve(['cat', 'calf', 'dog', 'bear']) == 'b'
	assert solve(['cat', 'calf', 'cog', 'dog', 'bear', 'bob']) == 'b'
