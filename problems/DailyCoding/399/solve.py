import itertools

from typing import List



def solve(integers: List[int], partition_count: int):
	count = len(integers)
	for indexes in itertools.product(*(range(count) for _ in range(partition_count))):
		for i, index in enumerate(indexes[:-1]):
			if index >= indexes[i+1]:
				break
		else:
			partitions = [integers[start:indexes[i + 1] if i + 1 < partition_count else count] for i, start in enumerate(indexes)]
			sums = list(map(sum, partitions))
			if all(sum == sums[0] for sum in sums[1:]):
				return partitions


def test_solve():
	assert solve([3, 5, 8, 1, 7], 3) == [[3, 5], [8], [1, 7]]
