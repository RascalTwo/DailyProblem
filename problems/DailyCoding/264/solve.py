import itertools

from typing import List, Optional, Set



def solve(characters: Set[str], k: int) -> Optional[str]:
	pool: List[str] = []
	for char in characters:
		for i in range(k):
			pool.append(char)

	for raw_order in set(itertools.permutations(set(itertools.permutations(pool, k)))):
		order: List[List[str]] = list(list(string) for string in raw_order)
		result_chars: List[str] = list(order[0])
		for string in order[1:]:
			for i in range(len(characters) - 1, 0, -1):
				if string[:i + 1] == result_chars[-i + -1:]:
					result_chars += list(string[i + 1:])
					break

		result_str = ''.join(result_chars)
		if not all(''.join(string) in result_str for string in order):
			continue

		# TODO - use last K added to remove trailing characters
		# to create cycle to front instead of 0s
		for i in range(len(result_chars) - 1, -1, -1):
			if result_chars[len(result_str) - 1 - i] == result_chars[i]:
				del result_chars[i]
			else:
				break

		if result_str != (closed_cycle := ''.join(result_chars)):
			return closed_cycle


def test_solve():
	assert solve({'0', '1'}, 3) in ['00010111', '11101000', '11010001', '00101110', '00111010', '11000101', '00011101']
