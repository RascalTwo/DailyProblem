import collections


from typing import DefaultDict, List



def count_common(a: int, b: int) -> int:
	length = max(a.bit_length(), b.bit_length())

	return sum(((a >> i) & 1) == ((b >> i) & 1) for i in range(length))


def solve(integers: List[int]) -> List[int]:
	totals: DefaultDict[int, int] = collections.defaultdict(int)
	for i, a in enumerate(integers):
		for j, b in enumerate(integers):
			if i == j:
				continue
			totals[i] += count_common(a, b)
	return [value for _, value in sorted(enumerate(integers), key = lambda pair: totals[pair[0]], reverse=True)]


def test_solve():
	assert solve([0b0000, 0b0110, 0b0101, 0b0111, 0b11111]) == [0b0111, 0b11111, 0b0110, 0b0101, 0b0000]
