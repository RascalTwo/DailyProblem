from typing import Dict, List, Optional


def solve(prerequisites: Dict[str, List[str]]) -> Optional[List[str]]:
	prereqs = sorted(prerequisites.items(), key = lambda pair: len(pair[1]))
	taken = []

	adding = True
	while adding:
		adding = False
		while prereqs and not prereqs[0][1]:
			adding = True
			taken.append(prereqs[0][0])
			del prereqs[0]

			last_taken = taken[-1]
			for _, dependencies in prereqs:
				if last_taken in dependencies:
					dependencies.remove(last_taken)
					for _, other_dependencies in prereqs:
						if last_taken in other_dependencies:
							other_dependencies.remove(last_taken)

			prereqs.sort(key = lambda pair: len(pair[1]))

		if not adding:
			break

	return taken if len(taken) == len(prerequisites) else None


def test_solve():
	assert solve({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}) == ['CSC100', 'CSC200', 'CSC300']
	assert solve({'B': ['A'], 'C': ['B', 'A'], 'A': []}) == ['A', 'B', 'C']
	assert solve({'B': ['A'], 'C': ['B', 'A', 'D'], 'A': []}) == None
	assert solve({'B': ['A'], 'C': ['B', 'A'], 'A': ['0']}) == None
