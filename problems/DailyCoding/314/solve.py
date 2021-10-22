import itertools
import sys

from typing import List



def solve_iter(listeners: List[int], towers: List[int]) -> int:
	for distance in itertools.count(1):
		receiving = [False] * len(listeners)
		for tower in towers:
			tower_range = range(tower - distance, tower + distance + 1)
			for i, listener in enumerate(listeners):
				if listener in tower_range:
					receiving[i] = True

			if all(receiving):
				return distance


def solve_calculate(listeners: List[int], towers: List[int]) -> int:
	return max((min(abs(listener - tower) for tower in towers) for listener in listeners), default=0)


def solve_calculate_readable(listeners: List[int], towers: List[int]) -> int:
	longest_distance = -sys.maxsize

	for listener in listeners:

		shortest_distance = sys.maxsize
		for tower in towers:
			distance = abs(listener - tower)
			if distance < shortest_distance:
				shortest_distance = distance

		if shortest_distance > longest_distance:
			longest_distance = shortest_distance

	return longest_distance


def test_solve():
	for solve in (solve_iter, solve_calculate, solve_calculate_readable):
		assert solve([1, 5, 11, 20], [4, 8, 15]) == 5
