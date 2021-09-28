from typing import List

def are_together(positions: List[int]) -> bool:
	for i, pos in enumerate(positions):
		if pos != i + positions[0]:
			return False
	return True


def solve(seats: List[int]) -> int:
	people: List[int] = []
	for i, seat in enumerate(seats):
		if seat == 1:
			people.append(i)

	center_index = people[len(people) // 2]
	traversed = 0
	looking_distance = 1
	while not are_together(people):
		furthest_i = max(range(len(people)), key = lambda i: abs(people[i] - center_index))

		look_first = 'left' if sum(pos < center_index for pos in people) > sum(pos > center_index for pos in people) else 'right'

		empty_seat = None if seats[center_index] == 1 else center_index
		while empty_seat is None:
			left = center_index - looking_distance
			right = center_index + looking_distance
			first, second = [left, right] if look_first == 'left' else [right, left]
			for pos in (first, second):
				if seats[pos] == 0:
					empty_seat = pos
					break
			looking_distance += 1

		traversed += abs(people[furthest_i] - empty_seat)

		seats[people[furthest_i]] = 0
		seats[empty_seat] = 1

		del people[furthest_i]
		people.append(empty_seat)
		people.sort()

	return traversed


def test_solve():
	assert solve([0, 1, 1, 0, 1, 0, 0, 0, 1]) == 5
	assert solve([1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]) == 18
