import itertools

from typing import List, Tuple



def sieve(n: int) -> List[int]:
	primes: List[int] = [i for i in range(2, n)]

	i = 0
	while i < len(primes):
		factor = 1
		multiple = 0
		while multiple < n:
			factor += 1
			multiple = primes[i] * factor
			if multiple in primes:
				primes.remove(multiple)
		i += 1

	return primes


def solve(goal: int) -> Tuple[int, int]:
	for combo in itertools.product(sieve(goal), repeat=2):
		if sum(combo) == goal:
			return combo  # type: ignore
	return 0, 0


def test_solve():
	assert solve(4) == (2, 2)
	assert solve(9) in [(2, 7), (7, 2)]
