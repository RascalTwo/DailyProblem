import random
import collections


from typing import Counter, List



def solve(numbers: List[int], probabilities: List[float]) -> int:
	most = None
	while not most:
		r = random.random()
		for prob in probabilities:
			if prob < r and (most is None or most < prob):
				most = prob
	return numbers[random.choice([i for i, prob in enumerate(probabilities) if prob == most])]


def test_solve():
	counts: Counter[int] = collections.Counter()
	for _ in range(1000000):
		counts[solve([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])] += 1
	print(counts)

