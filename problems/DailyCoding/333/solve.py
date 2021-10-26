import random

from typing import Callable, Dict, List, Tuple



def solve(people: List[str], knows: Callable[[str, str], bool]):
	stack = people[::]
	while len(stack) > 1:
		a, b = stack.pop(), stack.pop()
		if knows(a, b):
			stack.append(b)
		else:
			stack.append(a)

	celeb = stack.pop()

	for person in people:
		if person == celeb:
			continue
		if knows(celeb, person) or not knows(person, celeb):
			return None

	return celeb


def generate_celebrity(people: List[str], celebrity: str) -> Tuple[List[str], Callable[[str, str], bool]]:
	stable_results: Dict[str, bool] = {}
	def knows(a: str, b: str) -> bool:
		if a == celebrity:
			return False
		if b == celebrity:
			return True
		return stable_results.setdefault(f'{a}->{b}', bool(random.randint(0, 1)))

	return people, knows

def test_solve():
	assert solve(*generate_celebrity(['a', 'b', 'c', 'd', 'E', 'f', 'g', 'h'], 'E')) == 'E'
	assert solve(*generate_celebrity(['a', 'b', 'c', 'd', 'E', 'f', 'g', 'h'], 'G')) is None
