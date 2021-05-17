from typing import List, Tuple



def transactions_to_profit(prices: List[int], transactions: List[Tuple[int, int]]) -> int:
	profit = len(transactions) * -2
	for bi, si in transactions:
		profit += prices[si] - prices[bi]
	return profit


def solve(prices: List[int], transactions: List[Tuple[int, int]] = []) -> int:
	best: int = transactions_to_profit(prices, transactions)

	start_index = transactions[-1][1] + 1 if transactions else 0
	for i, buy in enumerate(prices[start_index:], start_index):
		for j, sell in enumerate(prices[i + 1:], i + 1):
			if buy < sell:
				best = max(best, solve(prices, transactions + [(i, j)]))

	return best


def test_solve():
	assert solve([1, 3, 2, 8, 4, 10]) == 9
