from typing import Callable, List



def generate_sum(l: List[int]) -> Callable[[int, int], int]:
	return lambda i, j: sum(l[i:j])


def test_solve():
	sum = generate_sum([1, 2, 3, 4, 5])
	assert sum(1, 3) == 5
	assert sum(0, 5) == 15
