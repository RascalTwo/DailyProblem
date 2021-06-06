from typing import Iterable, List



def solve(digits: str, created: List[int] = []) -> Iterable[List[int]]:
	if len(created) == 4:
		if not digits:
			yield created[::-1]
		return

	length_m1 = len(digits) - 1
	for i in range(min(length_m1, 2), -1, -1):
		considering = digits[length_m1 - i:]

		if not (considering[0] == '0' and len(considering) > 1) and (number := int(considering)) <= 254:
			yield from solve(digits[:-i+-1], created + [number])


def test_solve():
	assert list(solve('2542540123')) == [[254, 25, 40, 123], [254, 254, 0, 123]]
	assert list(solve('128128128128')) == [[128, 128, 128, 128]]
	assert list(solve('10101010')) == [
		[10, 10, 10, 10],
		[101, 0, 10, 10],
		[10, 101, 0, 10],
		[10, 10, 101, 0],
		[101, 0, 101, 0]
	]
