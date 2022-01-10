import statistics

from typing import List



def solve(*arrays: List[int]) -> float:
	array: List[int] = []
	indexes: List[List[int]] = [[i, 0, len(arrays[i])] for i in range(len(arrays)) if arrays[i]]
	while indexes:
		values = {ii: arrays[i][vi] for ii, (i, vi, _) in enumerate(indexes)}
		index, value = min(values.items(), key = lambda item: item[1])
		array.append(value)
		indexes[index][1] += 1
		if indexes[index][1] == indexes[index][2]:
			indexes.pop(index)
	return statistics.median(array)



def test_solve():
	assert solve([1, 3], [2]) == 2
	assert solve([1, 2], [3, 4]) == 2.5
	assert solve([1, 3], [2], []) == 2