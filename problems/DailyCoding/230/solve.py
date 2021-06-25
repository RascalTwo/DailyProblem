import sys
import functools


@functools.lru_cache(maxsize=None)
def solve(eggs: int, floors: int) -> int:
	if eggs <= 1 or floors <= 1:
		return floors

	drops = sys.maxsize
	for floor in range(1, floors + 1):
		drops = min(
			drops,
			max(
				solve(eggs - 1, floor - 1),
				solve(eggs, floors - floor)
			)
		)

	return drops + 1


def test_solve():
	assert solve(1, 5) == 5
	assert solve(2, 5) == 3
	assert solve(2, 10) == 4
