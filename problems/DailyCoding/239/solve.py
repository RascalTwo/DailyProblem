import itertools

from typing import Dict, Iterable, List, Tuple



def is_pattern_valid(keypad: List[List[int]], pattern: List[int]) -> bool:
	locations: Dict[int, Tuple[int, int]] = {}
	for r, row in enumerate(keypad):
		for c, value in enumerate(row):
			locations[value] = (r, c)

	used: List[int] = []
	used.append(pattern.pop(0))
	while pattern:
		current = pattern.pop(0)
		last_loc = locations[used[-1]]
		curr_loc = locations[current]
		change = curr_loc[0] - last_loc[0], curr_loc[1] - last_loc[1]
		greatest_divisor = max(abs(ch) for ch in change)
		offset = change[0] / greatest_divisor, change[1] / greatest_divisor

		jumping: List[Tuple[int, int]] = []

		start: Tuple[float, float] = last_loc[0] + offset[0], last_loc[1] + offset[1]
		while start != curr_loc:
			if (start_int := (int(start[0]), int(start[1]))) in locations.values():
				jumping.append(start_int)
			start = start[0] + offset[0], start[1] + offset[1]

		if any(val not in used for loc in jumping if (val := keypad[loc[0]][loc[1]])):
			return False

		used.append(current)

	return True


def solve(keypad: List[List[int]], n: int) -> Iterable[List[int]]:
	values =  [value for row in keypad for value in row]
	for pattern in itertools.permutations(values, n):
		pattern = list(pattern)
		if is_pattern_valid(keypad, pattern[:]):
			yield pattern


def test_solve():
	one_to_nine = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	assert len(list(solve(one_to_nine, 1))) == 9
	assert len(list(solve(one_to_nine, 2))) == 40
	assert len(list(solve(one_to_nine, 3))) == 192
	assert len(list(solve(one_to_nine, 4))) == 834
	assert len(list(solve(one_to_nine, 5))) == 3280
	assert len(list(solve(one_to_nine, 6))) == 11042
	assert len(list(solve(one_to_nine, 7))) == 29454
	assert len(list(solve(one_to_nine, 8))) == 55616
	assert len(list(solve(one_to_nine, 9))) == 55616
	assert is_pattern_valid(one_to_nine, [4, 2, 1, 7]) is True
	assert is_pattern_valid(one_to_nine, [2, 1, 7]) is False
