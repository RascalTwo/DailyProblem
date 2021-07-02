import random

from typing import List



def random_int(k: int) -> int:
	return random.randint(1, k)


def solve(cards: List[int]) -> None:
	for i in range(len(cards) - 1, 0, -1):
		j = random_int(i + 1) - 1
		cards[i], cards[j] = cards[j], cards[i]


def test_solve():
	deck = [i for i in range(1, 53)]
	shuffled = deck[:]
	solve(shuffled)
	print(shuffled)
