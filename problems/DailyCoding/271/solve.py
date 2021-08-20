import random

from typing import Iterable, List



def generate_powers_of_two(count: int) -> Iterable[int]:
	last = 1
	for _ in range(1, count):
		yield last
		last = last + last


POWERS_OF_TWO = list(generate_powers_of_two(12))


def solve(haystack: List[int], needle: int) -> bool:
	length = len(haystack)
	p_index = 0
	while POWERS_OF_TWO[p_index + 1] < length:
		p_index += 1

	offset = 0
	while p_index != -1:
		middle = offset + POWERS_OF_TWO[p_index]
		p_index -= 1
		if middle >= length:
			continue

		value = haystack[middle]
		if value == needle:
			return True
		if value < needle:
			offset = middle

	return haystack[0] == needle

def test_solve():
	assert solve([0, 1, 2, 3, 4], 0) is True
	assert solve([0, 1, 2, 3], 0) is True
	assert solve([0, 1, 2, 3, 4], 4) is True
	assert solve([0, 1, 2, 3], 3) is True

	for n in (10, 100, 1000):
		sample = sorted([random.randint(0, n) for _ in range(n)])
		target = random.choice(sample)
		assert solve(sample, target) is True
		assert solve(sample, n + 1) is False

