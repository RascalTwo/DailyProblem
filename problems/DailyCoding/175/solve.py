import collections
import random


from typing import Counter, DefaultDict, Dict, List, Tuple



Transition = Tuple[str, str, float]


def solve(transitions: List[Transition], state: str, num_steps: int) -> Dict[str, int]:
	transition_map: DefaultDict[str, DefaultDict[str, float]] = collections.defaultdict(lambda: collections.defaultdict(float))
	for origin, dest, probability in transitions:
		transition_map[origin][dest] = probability


	counts: Counter[str] = collections.Counter()

	for _ in range(num_steps):
		options = transition_map[state]
		state = random.choices(list(options.keys()), list(options.values()))[0]
		counts[state] += 1

	return counts


def test_solve():
	result = solve([
		('a', 'a', 0.9),
		('a', 'b', 0.075),
		('a', 'c', 0.025),
		('b', 'a', 0.15),
		('b', 'b', 0.8),
		('b', 'c', 0.05),
		('c', 'a', 0.25),
		('c', 'b', 0.25),
		('c', 'c', 0.5)
	], 'a', 5000)
	assert 2800 <= result['a'] <= 3400
	assert 1200 <= result['b'] <= 1900
	assert 200 <= result['c'] <= 400