from typing import List



def solve(prices: List[int]) -> int:
	best = (0, 0)

	for i, buy in enumerate(prices):
		if profit := max(prices[i:]) - buy > best[1]:
			best = (buy, profit)

	return best[0]


def test_solve():
	assert solve([9, 11, 8, 5, 7, 10]) == 5
