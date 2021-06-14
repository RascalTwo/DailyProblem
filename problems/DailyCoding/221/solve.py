import itertools


from typing import List



def solve(n: int) -> int:
	sevens: List[int] = []
	powers: List[int] = []
	while len(sevens) < n + 1:
		powers.append(7**len(powers))
		sevens.append(powers[-1])
		for size in range(2, len(powers) + 1):
			for combination in itertools.combinations(powers, size):
				if powers[-1] in combination and (considering := sum(combination)) not in sevens:
					sevens.append(considering)

	return sevens[n]

def test_solve():
	assert solve(0) == 1
	assert solve(1) == 7
	assert solve(2) == 8
	assert solve(3) == 49
	assert solve(10) == 392
