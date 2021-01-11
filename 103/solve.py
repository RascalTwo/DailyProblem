from typing import Optional, Set



def solve(string: str, characters: Set[str]) -> Optional[str]:
	shortest = None
	for i in range(len(string) - len(characters)):
		found = set(string[i:i + len(characters)-1])

		for j in range(i+len(characters), len(string)):
			found.add(string[j])
			if found.intersection(characters) == characters:
				if shortest is None or len(string[i:j+1]) < len(shortest):
					shortest = string[i:j+1]

	return shortest


def test_solve():
	assert solve('figehaeci', {'a', 'e', 'i'}) == 'aeci'
	assert solve('hello world', {'l', 'd', 'z'}) == None
