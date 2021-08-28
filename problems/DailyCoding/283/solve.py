import functools

from typing import Iterable


@functools.lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
	if n <= 1:
		return False
	for i in range(2, (n // 2) + 1):
		if n % i == 0:
			return False
	return True


def get_prime_divisors(n: int) -> Iterable[int]:
	for i in range(1, (n // 2) + 1):
		if n % i == 0 and is_prime(i):
			yield i


def solve(n: int) -> Iterable[int]:
	next = 0
	for _ in range(n):
		while True:
			next += 1
			if next <= 5 or (divisors := list(get_prime_divisors(next))) and all(divisor <= 5 for divisor in divisors):
				yield next
				break



def test_solve():
	assert list(solve(30)) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54, 60, 64, 72, 75, 80]
