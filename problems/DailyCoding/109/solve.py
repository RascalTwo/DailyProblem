import operator


from typing import Any, Callable



noop: Callable[[Any], Any] = lambda v: v


def solve(num: int):
	bits = num.bit_length()

	for n in range(0, bits + (bits & 1), 2):
		pair = [(num >> (n + i)) & 1 for i in range(2)]
		if pair[0] == pair[1]:
			continue

		for i, v in enumerate(pair):
			num = (operator.and_ if v else operator.or_)(num, [noop, operator.inv][v](1 << (n + i)))

	return num


def test_solve():
	assert solve(0b10101010) == 0b01010101
	assert solve(0b11100010) == 0b11010001
	assert solve(0b10010) == 0b100001
