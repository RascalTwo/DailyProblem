import sys
import math
import itertools


from typing import List, Tuple



def solve(numbers: List[float]) -> List[int]:
	expected_sum = sum(numbers)

	best: Tuple[float, List[int]] = (sys.maxsize, [])
	for ops in itertools.product([math.ceil, math.floor], repeat=len(numbers)):
		possible = [op(numbers[i]) for i, op in enumerate(ops)]
		if sum(possible) != expected_sum:
			continue

		differences = sum(abs(numbers[i] - possible[i]) for i in range(len(numbers)))
		if differences < best[0]:
			best = (differences, possible)

	return best[1]

def test_solve():
	assert solve([1.3, 2.3, 4.4]) == [1, 2, 5]
