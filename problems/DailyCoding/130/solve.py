from typing import List, Tuple



def solve(prices: List[int], k: int, transactions: List[Tuple[int, int]] = []) -> int:
	best = sum(prices[sell] - prices[buy] for buy, sell in transactions)
	if k == 0:
		return best

	for buy in range(next((sell + 1 for _, sell in transactions), 0), len(prices) - 1):
		for sell in range(buy + 1, len(prices)):
			if prices[buy] > prices[sell]:
				continue
			best = max(best, solve(prices, k - 1, transactions + [(buy, sell)]))

	return best


def test_solve():
	assert solve([5, 2, 4, 0, 1], 2) == 3
	assert solve([5, 0, 10], 1) == 10
	assert solve([7, 5, 3, 10, 20], 3) == 17
