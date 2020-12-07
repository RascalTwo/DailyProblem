from typing import List, Optional



def solve(integers: List[int], target: int) -> Optional[int]:
	if integers[0] == target:
		return 0

	index = 0
	direction = 1 if integers[0] < target else -1
	while True:
		current = integers[index]
		if current == target:
			return index if index > 0 else len(integers) + index
		if (direction == 1 and current > target) or (direction == -1 and current < target):
			return None

		index += direction


def test_solve():
	assert solve([13, 18, 25, 2, 8, 10], 8) == 4
	assert solve([13, 18, 25, 2, 8, 10], 25) == 2
	assert solve([13, 18, 25, 2, 8, 10], 7) is None
