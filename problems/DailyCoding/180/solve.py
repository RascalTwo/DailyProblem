from typing import List



def solve(stack: List[int]) -> List[int]:

	queue: List[int] = []
	for remaining in range(len(stack) - 1, 1, -1):
		for _ in range(remaining):
			queue.append(stack.pop())
		for _ in range(remaining):
			stack.append(queue.pop(0))

	return stack


def test_solve():
	assert solve([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
	assert solve([1, 2, 3, 4,]) == [1, 4, 2, 3]
