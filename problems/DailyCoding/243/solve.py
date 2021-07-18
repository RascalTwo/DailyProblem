from typing import List, Optional



def group_with_limit(numbers: List[int], limit: int, k: int) -> Optional[List[List[int]]]:
	groups: List[List[int]] = [[]]
	for number in numbers:
		if sum(groups[-1]) + number > limit:
			groups.append([number])
		else:
			groups[-1].append(number)


	while True:
		group_count = len(groups)
		if group_count == k:
			return groups

		for i, group in enumerate(groups):
			if len(group) > 1:
				groups.insert(i, [group.pop(0)])
				break
		else:
			break


	return groups if group_count == k else None


def solve(numbers: List[int], k: int) -> List[List[int]]:
	return next(
		partitions
		for maximum in range(max(numbers), sum(numbers))
		if (partitions := group_with_limit(numbers, maximum, k))
	)

def test_solve():
	assert solve([5, 1, 2, 7, 3, 4], 3) == [[5, 1, 2], [7], [3, 4]]

	assert solve([1, 2, 3], 3) == [[1], [2], [3]]
	assert solve([1, 2, 3], 2) == [[1, 2], [3]]
