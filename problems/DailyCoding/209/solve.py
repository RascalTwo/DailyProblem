
import itertools
import copy


from typing import Any, List, Sequence



def solve(*strings: str) -> int:
	lengths = [len(string) + 1 for string in strings]

	longests: List[Any] = [0 for _ in range(lengths[-1])]
	for length in lengths[:-1][::-1]:
		longests = [copy.deepcopy(longests) for _ in range(length)]

	def set_at_indexes(indexes: Sequence[int], value: int):
		setting = longests
		for i in indexes[:-1]:
			setting = setting[i]

		setting[indexes[-1]] = value

	def get_at_indexes(indexes: Sequence[int]) -> int:
			value = longests
			for i in indexes:
				value = value[i]

			assert isinstance(value, int)
			return value

	for indexes in itertools.product(*(range(length) for length in lengths)):
		if len({
			string[indexes[si] - 1]
			for si, string in enumerate(strings)
		}) == 1:
			set_at_indexes(indexes, get_at_indexes([i - 1 for i in indexes]) + 1)
			continue

		offsets: List[List[int]] = [list(indexes) for _ in range(len(indexes))]
		for o in range(len(indexes)):
			offsets[o][o] -= 1

		set_at_indexes(indexes, max(get_at_indexes(offset) for offset in offsets))

	return get_at_indexes([length - 2 for length in lengths])


def test_solve():
	assert solve('abc', 'abc', 'abc') == 3
	assert solve('a', 'bc', 'def') == 0
	assert solve('abc', 'ac', 'bc') == 1
	assert solve('epidemiologist', 'refrigeration', 'supercalifragilisticexpialodocious') == 5
	assert solve('abcd', 'abcd', 'abcd', 'abcd') == 4
