import itertools

from typing import Dict, Iterable, List



def solve_infinite() -> Iterable[int]:
	non_primes: Dict[int, List[int]] = {}

	start = 1
	while True:
		start += 1

		if start not in non_primes:
			yield start
			non_primes[start * start] = [start]
			continue
		for divisor in non_primes[start]:
			non_primes.setdefault(start + divisor, []).append(divisor)


def solve(n: int) -> List[int]:
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


def test_solve():
	primes_under_twenty = [2, 3, 5, 7, 11, 13, 17, 19]
	assert solve(20) == primes_under_twenty
	assert list(itertools.islice(solve_infinite(), 8)) == primes_under_twenty
